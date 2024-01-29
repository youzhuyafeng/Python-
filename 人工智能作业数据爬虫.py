from lxml import etree
import requests
import re
import jsonlines
import time
import random


# 初始化jsonl字典列表，字典为{"src":[""] ,"tgt":[""]}格式
data_list = []


# 发送请求函数
# 已测试，正常
def get_response(url, headers):
    response = requests.get(url=url, headers=headers)
    response.encoding = "gbk"
    content = response.text
    return content


# xpath提取文章超链接函数，返回超链接列表
# 已测试，正常
def get_art_SuperLink(content):
    tree = etree.HTML(content)
    SuperLink = tree.xpath('//div[@class="main_left"]/ul[@class="list"]/li/span/a/@href')
    return SuperLink


path1 = '//div[@class="main_left"]/ul[@class="list"]/li/span/a/@href'
path2 = '//*[@id="article_content"]/div/div/span/text()'
path3 = '//*[@id="article_content"]/div/div/text()'
path4 = '//div[@style="margin: 0px auto; padding: 0px; text-align: left;" ]/text()'
path5 = '//div[@style="margin: 0px auto; padding: 0px; text-align: left;" ]/text()'


# xpath提取文章内容函数列表，多种xpath结构，如果是空列表就换另一个
# 已测试，正常
def get_art_content(SuperLink,path):
    art_response = get_response(SuperLink, headers)
    tree = etree.HTML(art_response)
    art_content = tree.xpath(path)
    return art_content


# 处理获取的内容，使列表内容链接成字符串，注意输出结果为字符串
# 已测试，正常
def art_link(art_content):
    art_str = ""
    for content in art_content:
        art_str += content
    return art_str


# 获取文章标题列表，列表只有一个元素
# 已测试，正常
def get_art_title(SuperLink):
    art_response = get_response(SuperLink, headers)
    tree = etree.HTML(art_response)
    art_title = tree.xpath('//*[@id="content"]/h1/text()')
    return art_title


# 正则表达式标准化文章标题,注意输出结果是字符串
# 已测试，正常
def std_title(art_title):
    pattern = re.compile("(?:范文：|期：|指导：|技巧：|预测：|申论：|备考：|赏析：)(.*)")
    title = re.search(pattern, art_title[0]).group(1)
    std_title = "请以"+title+"为标题写一篇申论"
    return std_title


# 构造jsonl问答字典函数,注意art_str要组合成列表才能使用
# 已测试，正常
def jsonl_dict(std_title,art_str):
    data_dict = {"src": [std_title], "tgt": [art_str]}
    data_list.append(data_dict)
    return None

# 写入jsonl文件函数
# 已测试，正常
def write_jsonl(data_list):
    jsonl_file = r"D:\essay_productor.jsonl"
    with jsonlines.open(jsonl_file, mode='a') as writer:
        for data in data_list:
            writer.write(data)
    return None


# 请求头参数
total_url = "http://www.chinagwyw.org/slfd/sllw/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
           "Cookie": "__51vcke__JkEAr3SeUbZ4vRZD=ea54c43a-3726-5c10-a50b-dcce5860ffcc; __51vuft__JkEAr3SeUbZ4vRZD=1703933968243; __51cke__=; __51uvsct__JkEAr3SeUbZ4vRZD=3; __tins__15582185=%7B%22sid%22%3A%201703996270446%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201703998406981%7D; __51laig__=3; __vtins__JkEAr3SeUbZ4vRZD=%7B%22sid%22%3A%20%22ba920228-541e-5a3e-93f9-a2acfaa30b71%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%20336475%2C%20%22dr%22%3A%2031616%2C%20%22expires%22%3A%201703998407155%2C%20%22ct%22%3A%201703996607155%7D"
           }


# 循环体，外层循环为页数循环，内层循环为获取文章内容
for page in range(1, 10):
    # 发起请求
    if page == 1:
        content = get_response(url=total_url, headers=headers)
    else:
        url = total_url+"list_"+str(page)+".html"
        content = get_response(url=url, headers=headers)
    # 获取每篇文章超链接，返回超链接列表
    SuperLink_list = get_art_SuperLink(content)
    for SuperLink in SuperLink_list:
        # 标题标准化，返回字符串
        art_title = get_art_title(SuperLink)
        standard_title = std_title(art_title)
        # 内容标准化，返回字符串
        art_content = get_art_content(SuperLink, path1)
        # art_content如果为空列表或垃圾广告采用第二种获取内容方式，依此类推，如果仍然是空列表直接跳过，链接为字符串
        if (not art_content) or len(art_content[0]) < 100:
            art_content = get_art_content(SuperLink, path2)
        if (not art_content) or len(art_content[0]) < 100:
            art_content = get_art_content(SuperLink, path3)
        if (not art_content) or len(art_content[0]) < 100:
            art_content = get_art_content(SuperLink, path4)
        if (not art_content) or len(art_content[0]) < 100:
            art_content = get_art_content(SuperLink, path5)
        if art_content:
            jsonl_dict(standard_title, art_link(art_content))
        else:
            continue
        time.sleep(random.uniform(0.5, 1))
# 写入jsonl文件
jsonl_file = "申论爬虫.jsonl"
with jsonlines.open(jsonl_file, mode='a') as writer:
    for i in data_list:
        writer.write(i)






