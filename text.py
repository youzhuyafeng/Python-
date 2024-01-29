import requests
import pandas as pd
import time
import jsonpath
import json
import re


first_url = "https://weibo.com/ajax/statuses/buildComments?"
first_params = {
    'is_reload': '1',
    'id': '4958093727499347',
    'is_show_bulletin': '2',
    'is_mix': '0',
    'count': '10',
    'uid': '2656274875',
    'fetch_level': '0',
    'locale': 'zh-CN'
}
first_headers = {
    'path': '/ajax/statuses/buildComments?flow=0&is_reload=1&id=4958093727499347&is_show_bulletin=2&is_mix=0&max_id=141207674567259&count=20&uid=2656274875&fetch_level=0&locale=zh-CN',
    'scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Client-Version': 'v2.44.29',
    'Cookie': 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFKPZVGxDCcavkcXZnkU-355JpX5KMhUgL.FoqXSoM0e0.N1hM2dJLoIEBLxK-LBo.LB.BLxKMLB-zLBo.LxK.L1-zL1h-LxK.LBKeL12-t; ALF=1703426422; SSOLoginState=1700834423; SCF=AvUEFv-hFEnvsn6hlsnE_rJSaU7CjUbhVV4DbNA1GISKt5ZYxBienVf1k2zaCCaslmh_iEVY1Xr4ovjcseICzi8.; SUB=_2A25IZNwnDeRhGeBK7VUS8yfLwzuIHXVrGFHvrDV8PUNbmtAGLVaskW9NR48NBiUugYeRns2Su9I9-SK1tUCkkBct; XSRF-TOKEN=STGHBa3UwPyFRs1xNP3r4149; _s_tentry=www.weibo.com; Apache=7450614184319.089.1700834470842; SINAGLOBAL=7450614184319.089.1700834470842; ULV=1700834470856:1:1:1:7450614184319.089.1700834470842:; PC_TOKEN=b91b7147cc; WBPSESS=J7EfK1GvDnwUCC2ATC6o8gdTMLj4dfbtXPwzdzAIGiDLvKOVpdMi4p--Je1_pRM53S_Q1jNB_dmJnbjvo_i5hZ2kStwLXIiTH3sIvn8Wbf0C5biMiqbmKXx21KKhutwsBkVhjyGaln-PIkmRzdUPUQ==',
    'Referer': 'https://weibo.com/2656274875/NonhyvsVd',
    'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Server-Version': 'v2023.11.23.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Xsrf-Token': 'STGHBa3UwPyFRs1xNP3r4149'
}

response = requests.get(url=first_url, params=first_params, headers=first_headers)
response.encoding = 'utf-8'

a = response.json()  # 字典
print(type(a))
a1 = json.dumps(a, ensure_ascii=False)    #json字符串
with open('text.json', 'w', encoding='utf-8') as fp:
    fp.write(a1)

obj = json.loads(a1)
data_list = jsonpath.jsonpath(a, '$.data')
print(data_list[0][0])
text_list = []

for i in data_list[0]:
   text_list.append(i['text'])
print(text_list)
print(len(text_list))


list1 = [[[1, ], 2], [[3, ], 4], [[5, ], 6]]
for i, j in list1:
    print(i)
    print(type(i))

pattern = re.compile('\d\d\d', flags=re.I)
match_sub = pattern.search('13dfdns21e2'
                           '41')
print(match_sub)
d = 1


def func(k):
    global d
    d = 2
    k *= d
    return k


print(func(2))

for i in range(10):

    d = i
    print(d)

def isPalindrome(text):

    t_reverse = text[::-1]

    if t_reverse == text:

        print("yes")

    else:

        print("no")

isPalindrome("abcdcba")


def func1(x):

    if x == 0:  return 0

    else: return x + func1(x-1)

print(func1(5))
