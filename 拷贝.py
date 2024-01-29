import requests
import pandas as pd
import time
import jsonpath
import re
import random

name_list = []
comment_list = []
address_list = []
time_list = []
# 创建枝评论列表
branch_comment_list = []
id_list = []


def get_response(url, params, headers):
    # get方法获取响应
    response = requests.get(url=url, params=params, headers=headers)
    response.encoding = 'utf-8'
    return response


# 获取楼数据列表
def handle_json_data(response):
    # 响应返回response类json格式代码，用json方法进行处理，返回json字典
    content = response.json()
    # jsonpath方法对json对象进行查找筛选
    data_list = jsonpath.jsonpath(content, '$.data')
    # 声明使用全局变量
    global name_list, comment_list, address_list, time_list
    # data_list是一个嵌套列表，其中只有第一项列表有我们想要的数据
    for i in data_list[0]:
        # 索引追加，要是追加值None的话会keyError报错，捕获异常
        # 采用索引追加异常捕获而不是直接用jsonpath主要是因为直接爬出的列表如果有数据缺失会导致将来创立DF对象时数据表无法对齐失去数据准确性
        try:
            name_list.append(i['user']['screen_name'])
        except KeyError:
            name_list.append('未知')
    for i in data_list[0]:
        try:
            address_list.append(i['source'])
        except KeyError:
            address_list.append('未知')
    for i in data_list[0]:
        try:
            comment_list.append(i['text'])
        except KeyError:
            comment_list.append('未知')
    for i in data_list[0]:
        try:
            time_list.append(i['created_at'])
        except KeyError:
            time_list.append('未知')
    # 只对列表操作，因此无需返回任何值
    return None


# 获取楼中楼评论列表，函数与上类似
def handle_branch_comment(response):
    content = response.json()
    data_list = jsonpath.jsonpath(content, '$.data')
    global branch_comment_list
    for i in data_list[0]:
        try:
            branch_comment_list.append(i['text'])
        except KeyError:
            branch_comment_list.append('未知')
    return None


# 楼评论与楼中楼通用请求参数，不断变化，其中首页评论没有，次页max_id位于上一页json字典max_id键的值，jsonpath抓取即可
def get_max_id(response):
    content = response.json()
    # 唯一子节点名，直接寻找即可
    max_id = jsonpath.jsonpath(content, '$.max_id')
    return max_id


# 楼中楼请求参数，是主楼json字典中mid键的值，jsonpath抓取即可
def get_id(response):
    content = response.json()
    id = jsonpath.jsonpath(content, '$.data')
    global id_list
    for i in id[0]:
        id_list.append(i["mid"])
    return id_list


# 首个请求的参数
all_url = "https://weibo.com/ajax/statuses/buildComments?"
first_params = {
    'is_reload': '1',
    'id': '4977005205915668',
    'is_show_bulletin': '2',
    'is_mix': '0',
    'count': '10',
    'uid': '1676679984',
    'fetch_level': '0',
    'locale': 'zh-CN'
}
headers = {
    'Cookie': 'SINAGLOBAL=7450614184319.089.1700834470842; UOR=,,cn.bing.com; SCF=AvUEFv-hFEnvsn6hlsnE_rJSaU7CjUbhVV4DbNA1GISKcITskKRn6POllmng372oSA5KJqeMOr_tMM7IDRjEmHo.; SUB=_2A25IfWArDeRhGeBK7VUS8yfLwzuIHXVr8_3jrDV8PUNbmtAGLWOhkW9NR48NBmMOfOg40YiE--S1BvaIv_QBtD-R; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFKPZVGxDCcavkcXZnkU-355JpX5KMhUgL.FoqXSoM0e0.N1hM2dJLoIEBLxK-LBo.LB.BLxKMLB-zLBo.LxK.L1-zL1h-LxK.LBKeL12-t; ALF=1705024891; ULV=1702522683460:5:3:3:7660168420581.992.1702522683450:1702433009516; XSRF-TOKEN=pr_6uYr4Xx2I0_OYRqwRRtpK; WBPSESS=J7EfK1GvDnwUCC2ATC6o8gdTMLj4dfbtXPwzdzAIGiDLvKOVpdMi4p--Je1_pRM53S_Q1jNB_dmJnbjvo_i5he1V1GlFXwlSUT-ymKNBHhyqkDJfJJI1E2Jt9ttb03qpv2uSfTFkEwgzkKQJ7t8r3A==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}
# 首个楼中楼评论参数
branch_params = {
    'is_reload': '1',
    'id': '',
    'is_show_bulletin': '2',
    'is_mix': '1',
    'fetch_level': '1',
    'max_id': '0',
    'count': '20',
    'uid': '1676679984',
    'locale': 'zh-CN'
}


# 枝评论次页获取函数
def branch_comment_operation2(branch_max_id,k):
    next_branch_params = {
        'flow': '0',
        'is_reload': '1',
        'id': id[j],
        'is_show_bulletin': '2',
        'is_mix': '1',
        'fetch_level': '1',
        'max_id': str(branch_max_id[0]),
        'count': '20',
        'uid': '1676679984',
        'locale': 'zh-CN'
    }
    next_branch_response = get_response(url=all_url, params=next_branch_params,
                                        headers=headers)
    handle_branch_comment(next_branch_response)
    branch_max_id = get_max_id(next_branch_response)
    if branch_max_id[0] == 0:
        k = 7
    k += 1
    time.sleep(random.uniform(0.5, 1))

# 创建用于寻找数据的各个空列表备用
max_id = []
branch_max_id = []
# 外楼页循环
# 外部for循环，内部while循环原因：外部数量可以自己控制，内部楼中楼评论需要全爬，否则可能存在回复性评论缺失无法构成完整对话。
for i in range(2):
    # 第一页请求与之后请求参数不同，因此要用if分支，楼中楼请求同理
    if i == 0:
        # 外部循环对楼进行请求，内部循环对楼中楼进行请求
        first_response = get_response(url=all_url, params=first_params, headers=headers)
        handle_json_data(first_response)
        id = get_id(first_response)
        # 外部评论的循环
        for j in range(len(id)):
            # 外部评论第一个评论的第一页（内部）请求
            if j == 0:
                # sleep方法暂停执行，避免被发现是爬虫
                k = 1
                while k <= 6:
                    if k == 1:
                        # 因为id是直接用jsonpath取出的，因此id的列表结构为['','','',...]，索引方式如下：
                        branch_params['id'] = id[j]
                        first_branch_response = get_response(url=all_url, params=branch_params, headers=headers)
                        handle_branch_comment(first_branch_response)
                        branch_max_id = get_max_id(first_branch_response)
                        if branch_max_id[0] == 0:
                            break
                        k += 1
                        time.sleep(random.uniform(0.5, 1))
                    else:
                        branch_comment_operation2(branch_max_id=branch_max_id, k=k)


            else:
                # branch列表是jsonpath取出data后循环追加的，因此branch列表结构为[[''],[''],[''],['']....]
                k = 1
                while k <= 6:
                    if k == 1:
                        # 因为id是直接用jsonpath取出的，因此id的列表结构为['','','',...]，索引方式如下：
                        branch_comment_operation2(branch_max_id="0", k=k)

                    else:
                        branch_comment_operation2(branch_max_id=branch_max_id, k=k)

        # 放最后，用于判定是否有下一页
        max_id = get_max_id(first_response)
        if max_id[0] == 0:
            break

    else:
        next_params = {
            'flow': '0',
            'is_reload': '1',
            'id': '4977005205915668',
            'is_show_bulletin': '2',
            'is_mix': '0',
            'max_id': str(max_id[0]),
            'count': '20',
            'uid': '1676679984',
            'fetch_level': '0',
            'locale': 'zh-CN'
            }
        next_response = get_response(url=all_url, params=next_params, headers=headers)
        handle_json_data(next_response)
        id = get_id(next_response)
        time.sleep(random.uniform(0.5, 1))
        for j in range(len(id)):
            if j == 0:
                k = 1
                while k <= 6:
                    if k == 1:
                        # sleep方法暂停执行2s，避免被发现是爬虫
                        branch_comment_operation2(branch_max_id="0", k=k)
                    else:
                        branch_comment_operation2(branch_max_id=branch_max_id, k=k)

            else:
                k = 1
                while k <= 6:
                    if k == 1:
                        branch_comment_operation2(branch_max_id="0", k=k)
                    else:
                        branch_comment_operation2(branch_max_id=branch_max_id, k=k)
        max_id = get_max_id(next_response)
        if max_id[0] == 0:
            break
# 查看主楼数据量
print(len(name_list))
# 创建一个处理后的评论空列表备用
new_comment_list = []
# 分别筛选主楼评论和楼中楼评论，不用函数是因为函数体就两行而且只需要调用两次，不如复制粘贴。
pattern = re.compile("(回复)?(<.*>)?(:)?(.[^<]*)(<.*>)?")
for i in comment_list:
    try:
        # 使用正则表达式剔除评论中超链接部分
        # 第一组为超链接的标签头，第三组为标签尾，第二组为评论信息
        search_str = pattern.search(i).group(4)
        new_comment_list.append(search_str)
    except:
        new_comment_list.append('无有效的评论信息')

# 创建主楼DataFrame对象，转置为纵向列表
df1 = pd.DataFrame(data=[name_list, new_comment_list, address_list, time_list], index=['姓名', '评论', '地址', '评论时间'])
df1 = df1.T
df1.to_csv('楼评论.csv', encoding='utf_8_sig')
# 创建楼中楼DF对象
new_df_comment_list = []
for i in branch_comment_list:
    # 第一组为超链接的标签头，第三组为标签尾，第二组为评论信息
    search_str = pattern.search(i).group(4)
    new_df_comment_list.append(search_str)
df2 = pd.DataFrame(data=new_df_comment_list, columns=['楼中楼评论'])
df2.to_csv('楼中楼评论.csv', encoding='utf_8_sig')
