import requests
import re
import json
from pprint import pprint

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url = "https://www.acfun.cn/v/ac43615458"
session = requests.session()
resp = session.get(url=url,headers=headers)
html_data = resp.text
title = re.findall('"title":"(.*?)"',html_data)[1]
data = re.findall('window.videoInfo = (.*?);', html_data)[0]
m3u8 = json.loads(json.loads(data)["currentVideoInfo"]["ksPlayJson"])['adaptationSet'][0]['representation'][0]['url']
m3u8_data  = requests.get(url=m3u8, headers=headers).text
ts_list = re.findall(',\n(.*?)\n#E',m3u8_data,re.S)
for ts in ts_list:
    ts_url = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + ts
    print(ts_url)
    ts_content = requests.get(url=ts_url, headers=headers).content
    with open(f'{title}.mp4',mode="ab") as f:
        f.write(ts_content)

