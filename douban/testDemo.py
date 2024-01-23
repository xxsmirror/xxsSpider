import requests
from lxml import etree
import json
import csv
import re
import time

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
start=0
results=[]
tag='心理学'
for i in range(50):
    
    request=requests.get("https://book.douban.com/tag/{tag}?start={start}&type=S".format(start=start,tag=tag),headers=headers)
    request.encoding='utf-8'
    html=etree.HTML(request.content)
    start=start+20
   
    names=html.xpath("//div[@class='info']/h2/a")
    rates=html.xpath("//span[@class='rating_nums']")
    pjs=html.xpath("//span[@class='pl']")

    name_text=[]
    rates_text=[]
    pjs_text=[]
    pjs_num=[]
    for name in names:
        name_text.append(name.text.replace('\n', '').replace('\r', '').replace(' ',''))
    for rate in rates:
        rates_text.append(rate.text)
    for pj in pjs:
        pjs_text.append(pj.text.replace('\n', '').replace('\r', '').replace(' ',''))

    print(len(name_text))
    print(len(rates_text))
    print(len(pjs_text))
    
    for j in range(20):
        if pjs_text[j]=='(少于10人评价)' or pjs_text[j]=='(少于10人评价)''(目前无人评价)':
            rates_text.insert(j,'(空)')

    for text in pjs_text:
        if pjs_text=='(目前无人评价)':
            pjs_num.append(0)
        else:
            numbers=re.findall(r'\d+', text)
            numbers=[int(n) for n in numbers]
            
            number=0
            for i in range(len(numbers)):
                number=number+numbers[i]*10**(len(numbers)-1-i)
            pjs_num.append(number)
            
    
    for k in range(20):
        
        result={'name':name_text[k],'rate':rates_text[k],'pj':pjs_num[k]}
        results.append(result)
    

# results_json=json.dumps(results,ensure_ascii=False,indent=2)

csv_fp = open("D:\素材\其他\python\{tag}.csv".format(tag=tag), "w",encoding='utf-8',newline='')
writer=csv.writer(csv_fp)
for row in results:
    writer.writerow(row.values())
csv_fp.close()





