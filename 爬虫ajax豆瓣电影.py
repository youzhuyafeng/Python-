import urllib.request
import urllib.parse

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
def get_request(page):
    old_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"
    data = {
        "start": (page-1)*20,
        "limit": 20
    }
    new_data = urllib.parse.urlencode(data)
    url = old_url+new_data
    requests = urllib.request.Request(url, headers=headers)
    return requests
def get_response(request):
    handler = urllib.request.HTTPSHandler()
    opener = urllib.request.build_opener(handler)
    requests = opener.open(request)
    return requests


start_page = int(input("请输入起始页"))
end_page = int(input("请输入末尾页"))
for page in range(start_page, end_page+1):
    request = get_request(page)
    response = get_response(request)
    with open("爬虫豆瓣排行榜"+str(page)+".json", "w", encoding="utf-8") as fp:
        fp.write(response)
















