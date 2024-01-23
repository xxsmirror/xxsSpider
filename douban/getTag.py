import requests
from lxml import etree

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}


request=requests.get("https://book.douban.com/tag/?icn=index-nav",headers=headers)
request.encoding='utf-8'
html=etree.HTML(request.content)
tags=html.xpath("//td/a")
# tags=tags[5:]
tag_list=[]
for tag in tags:
    tag_list.append(tag.text)
print(tag_list)

