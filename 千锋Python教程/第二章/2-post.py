import urllib.request
import urllib.parse

url = "https://fanyi.baidu.com/v2transapi/"
formdata = {
    'from':'en',
    'to':'zh',
    'query':'word',
    'transtype':'translang',
    'simple_means_flag':'3',
    'sign':'924944.720417',
    'token':'7372a96d2a0aed2e7ab5aac09843ed82',
}

headers = {
    "Host": "fanyi.baidu.com",
    "X-Requested-With" : "XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)   Chrome/76.0.3809.100 Safari/537.36" ,
    # "Sec-Fetch-Mode: "cors",
    "Origin": "https://fanyi.baidu.com",
    "Sec-Fetch-Site": "same-origin",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047",
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BIDUPSID=542952F88DEAD855C9470B742229C72F; PSTM=1564987516; BAIDUID=F47DE1F2BC41F04F37D91527CD3D3D90:FG=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1567675815; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1567675815; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; APPGUIDE_8_0_0=1; __yjsv5_shitong=1.0_7_845c7b3cd4d6284af0b6a6c926d0c5b445ab_300_1567675818692_113.81.199.74_43c8645f; yjs_js_security_passport=7defe635c4f974eaafa8e741ce2bab46cbc71db7_1567675819_js',

}

request = urllib.request.Request(url, headers = headers)

formdata = urllib.parse.urlencode(formdata).encode()

response = urllib.request.urlopen(request,data = formdata)

# print(response.read().decode())
# print(response.read())
# 998 代表参数不全；997 表示数据校验失败
with open("word.html","wb") as f:
    f.write(response.read())