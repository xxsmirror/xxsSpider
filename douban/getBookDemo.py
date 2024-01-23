import requests
from lxml import etree
import csv
import re
import os

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36','Cookie':''}
request_tag=requests.get("https://book.douban.com/tag/?icn=index-nav",headers=headers)
request_tag.encoding='utf-8'
html_tag=etree.HTML(request_tag.content)
tags=html_tag.xpath("//td/a")
tag_list=[]
for tag in tags:
    tag_list.append(tag.text)
print(tag_list)
start=0
results=[]

print(tag_list)



have = []
files = os.listdir('D:\素材\其他\python\douban')
for file in files:
    have.append(file[:-4])
set_difference = set(tag_list[6:]) - set(have)
difference_list = list(set_difference)
print(difference_list)
print(len(difference_list))

# difference_list = ['通信']

for tag in difference_list:
    fc=[]
    for j in range(50):
        
        ff=0
        for i in range(3):
            try:
                print('执行第'+str(j+1)+'次')
                req_book = requests.get('https://book.douban.com/tag/{tag}?start={j}&type=S'.format(j=str(j*20),tag=tag), headers=headers,timeout=5)
                req_book.encoding = 'utf-8'
                html_book = etree.HTML(req_book.text)

                names=html_book.xpath("//div[@class='info']/h2/a")
                rates=html_book.xpath("//span[@class='rating_nums']")
                pjs=html_book.xpath("//span[@class='pl']")


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
                for text in pjs_text:
                        if text=='(目前无人评价)' or text=='(少于10人评价)':
                            pjs_num.append(0)
                        else:
                            numbers=re.findall(r'\d+', text)
                            numbers=[int(n) for n in numbers]
                        
                            number=0
                            for z in range(len(numbers)):
                                number=number+numbers[::-1][z]*10**(z)
                            pjs_num.append(number)
                
                
                for k in range(len(name_text)):
                    fc.append((name_text[k],rates_text[k],pjs_num[k]))
                zip_list=zip(name_text,rates_text,pjs_num)

                print(name_text)

                print(fc)

                print(len(set(fc)))
                print(len(fc))
                if  len(set(fc)) != len(fc):
                    ff = ff+1
                    break

                with open('D:\素材\其他\python\douban\\{tag}.csv'.format(tag=tag),'a',newline='',encoding='utf-8') as f:
                    writer=csv.writer(f)
                    for z in zip_list:
                        writer.writerow(z)
                        

                break

            except Exception as e:
                if i < 2:
                    print('请求失败，正在重试')
                else:
                    print(e)
        
        if ff==1:
            break
        print(ff)