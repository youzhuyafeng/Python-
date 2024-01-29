import requests
all_url = "https://weibo.com/ajax/statuses/buildComments?"
headers = {
    'Cookie': 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFKPZVGxDCcavkcXZnkU-355JpX5KMhUgL.FoqXSoM0e0.N1hM2dJLoIEBLxK-LBo.LB.BLxKMLB-zLBo.LxK.L1-zL1h-LxK.LBKeL12-t; ALF=1703426422; SSOLoginState=1700834423; SCF=AvUEFv-hFEnvsn6hlsnE_rJSaU7CjUbhVV4DbNA1GISKt5ZYxBienVf1k2zaCCaslmh_iEVY1Xr4ovjcseICzi8.; SUB=_2A25IZNwnDeRhGeBK7VUS8yfLwzuIHXVrGFHvrDV8PUNbmtAGLVaskW9NR48NBiUugYeRns2Su9I9-SK1tUCkkBct; XSRF-TOKEN=STGHBa3UwPyFRs1xNP3r4149; _s_tentry=www.weibo.com; Apache=7450614184319.089.1700834470842; SINAGLOBAL=7450614184319.089.1700834470842; ULV=1700834470856:1:1:1:7450614184319.089.1700834470842:; PC_TOKEN=b91b7147cc; WBPSESS=J7EfK1GvDnwUCC2ATC6o8gdTMLj4dfbtXPwzdzAIGiDLvKOVpdMi4p--Je1_pRM53S_Q1jNB_dmJnbjvo_i5hZ2kStwLXIiTH3sIvn8Wbf0C5biMiqbmKXx21KKhutwsBkVhjyGaln-PIkmRzdUPUQ==',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}
params = {
    'is_reload': '1',
    'id': '4958094875426982',
    'is_show_bulletin': '2',
    'is_mix': '1',
    'fetch_level': '1',
    'max_id': '0',
    'count': '20',
    'uid': '2656274875',
    'locale': 'zh-CN'
}
response = requests.get(url=all_url, headers=headers, params=params)
print(response.json())


