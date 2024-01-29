from lxml import etree
import urllib.request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
def get_request(num):
    old_url = 'https://sc.chinaz.com/tupian/fengjing_'
    url = old_url+str(num)+'.html'
    requests = urllib.request.Request(url=url, headers=headers)
    return requests

def get_response_content(request):
    response = urllib.request.urlopen(request)
    contents = response.read().decode('utf-8')
    return contents

def get_tree_list(content):
    tree = etree.HTML(content)
    tree_lists = tree.xpath('//img[@class="lazy"]/@data-original')
    return tree_lists

def get_name_list(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//img[@class="lazy"]/@alt')
    return name_list

for i in range(2, 10):
    request = get_request(i)
    content = get_response_content(request)
    tree_list = get_tree_list(content)
    name_list = get_name_list(content)
    print(tree_list, name_list)
    for num in range(0, len(tree_list)):
        jpg_url = "http:"+tree_list[num]
        filename = name_list[num]+".jpg"
        urllib.request.urlretrieve(jpg_url, filename=filename)







