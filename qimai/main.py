import requests
import json

headers = {
    "authority": "api.qimai.cn",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.qimai.cn",
    "pragma": "no-cache",
    "sec-ch-ua": "^\\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
cookies = {
    "gr_user_id": "8ac49c7e-c3ce-4bc7-91da-f34ad90aeb10",
    "AUTHKEY": "Jy0hgxcTjf6Hj^%^2BwoGNXpQtcCwVT8y8d99f0v8X5IS28LC8GGkn5ZYOpmtWhwiqnqwWR09zcihnHh9ZFbg707Q^%^2BNae4cdyuscSLFI3^%^2F^%^2Fh^%^2Batz5Fhvo29X0g^%^3D^%^3D",
    "ada35577182650f1_gr_last_sent_cs1": "qm20252261949",
    "synct": "1706785830.071",
    "syncd": "-2675",
    "USERINFO": "C^%^2FuTsa1D6TA0L7pVfaV0oEdAQQ53e^%^2FtXpBHZDvn7ak0oopGiHO9PFeCMDItlmo8pbNOgqfXwVaYyBDqGSNKLxiw8wNrskubSRV2PV4RZ^%^2BTy7Et562Ulq^%^2FCqkNCWYsAII4h^%^2BF7DtxAIjUN4EPHxiSVQ^%^3D^%^3D",
    "PHPSESSID": "qlf5o1pkdus9boui6gd5nh5khq",
    "qm_check": "A1sdRUIQChtxen8pI0dAMRcOUFseEHBeQF0JTjVBWDAIXEQaYhAQbF1FIRUJCBETVkQSGAlIBAhVVl4pTEBTFXNbQlxTQAshV1ZIDgolAGgCEElDaw06VktIPEo+BAYbEhUSV1AABQxKQltKGQceABUAGAhHGw^%^3D^%^3D",
    "ada35577182650f1_gr_session_id": "687545fa-16ce-4f91-b688-4d35ed64684f",
    "ada35577182650f1_gr_last_sent_sid_with_cs1": "687545fa-16ce-4f91-b688-4d35ed64684f",
    "ada35577182650f1_gr_session_id_sent_vst": "687545fa-16ce-4f91-b688-4d35ed64684f",
    "ada35577182650f1_gr_cs1": "qm20252261949"
}
url = "https://api.qimai.cn/rank/marketRank"
params = {
    "analysis": "ezE^%^2FUyUSOAN7cgcUKQgJQSgyNlU4WlVHUFkISwxYRA4DEzoZFxF1EgNWUVcKBVNXUlFOOVkG",
    "market": "4",
    "category": "168",
    "date": "2024-02-01"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
