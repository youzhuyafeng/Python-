import urllib.request
import urllib.parse
import json
headers = {
    'Cookie': '__bid_n=188b3202cf77b779764207; FPTOKEN=9x6ervyakbBv58ypTW9wdMaHOnKFATn1/A1EtMLCHPYgEIVQhnlzOWco8uuAatcT02NRd1/ra+fkwV7lWO2Px8wd+Ahxjyrlq/6q0FEKEXiwuJCVRJzlsJKVSC21fCOmz01KsCrGGy/ayOJ7fLjhx1VDfSwjybga53Go4wW1WtKJegieyJJ0EANp+F7XPFPbxMJ3sOt0+lTHlMZN7SLEGTo9dkPVMQTL/b5+nTweV9sqsGUlvAqq8U8ZbgEN26F+vLafcNYawRGnXRWAy4x53JEwq7dQSSumoh0/pP7ujnnMfqDHz9VLOm4cPPIfgcOt3ExXRn2z01thwl3FbmwoOEsI81Mx8mLhSg5yAzzMklCabz8iUgeGQZl/iVU30XGC00oneREYdf7lVUo8k5drGA==|ZOh3DAsLQNWBaAEevq9CAqQ4IbdbJfAsA5xW8HGIV+g=|10|46fb9276e10252a64ccdd30b8e3ea8a1; BAIDU_WISE_UID=wapp_1687098829936_144; ZFY=645MQ55NmWKRnc4ABxSzpBFjXS:BPwpJG5yCK17nusFQ:C; BIDUPSID=93BA5AF0F9AACA19EF06D450C67E27BA; PSTM=1697890642; BAIDUID=F4777D98CADA4B13C134ACFB91B48E80:FG=1; BAIDUID_BFESS=F4777D98CADA4B13C134ACFB91B48E80:FG=1; jsdk-uuid=4f49614f-9b37-4dbb-9a58-43116e023569; BDUSS=3VzRkhqNWVXc09zfnZQQVpPeXREdHRTb3ZxUGZ4WTZNUTlhWlN0azF0M3FSR2hsRVFBQUFBJCQAAAAAAQAAAAEAAADu8MNC08TW8dHFt-e1xLnKysIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOq3QGXqt0Blc; BDUSS_BFESS=3VzRkhqNWVXc09zfnZQQVpPeXREdHRTb3ZxUGZ4WTZNUTlhWlN0azF0M3FSR2hsRVFBQUFBJCQAAAAAAQAAAAEAAADu8MNC08TW8dHFt-e1xLnKysIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOq3QGXqt0Blc; APPGUIDE_10_6_6=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=2k012g8la585a50ha12la5a41ikc6ug1r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1698992534,1699158681; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1699158996; Hm_lpvt_246a5e7d3670cfba258184e42d902b31=1699158997; RT="z=1&dm=baidu.com&si=872faa76-63a2-42dd-b2b1-5aa9d7bd26d1&ss=lokzei2x&sl=1&tt=2dp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=35w&ul=5wg&hd=5wv"; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1699161264; ab_sr=1.0.1_MTM5YTY2OGNjOWY0N2NjNzI2MjY3Y2UxNDFiMjM0NzViNmRlOGQ2ZTkyYzczYjY3MWZjMzA1MWQ1MGNjNjIwNDY1MmViZmRlMzM4OTRlNWMxMDdhZjQzMDI4MDQwZDU4NDg4ZWM5MGUxMDE0NjMzYjIzNTdjNGI0YmZmNTk3YmIxYmRhOTM2NzgwNmY4ZmUxYzE0NjllYjUyNWU0MjAzMzEwMjJjMWFiZjAwYWY1YTkyZjAxYzUxYTgwODExYzc4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}
data = {
    "from": "en",
    "to": "zh",
    "query": "love",
    "simple_means_flag": "3",
    "sign": "198772.518981",
    "token": "ff59f2178aac24c63771801df2b3c071",
    "domain": "common"
}
url = "https://fanyi.baidu.com/v2transapi"
data = urllib.parse.urlencode(data).encode("utf-8")
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
contents = str(json.loads(content))
print(contents)
with open("百度翻译.json", "w", encoding="utf-8") as fp:
    fp.write(contents)



