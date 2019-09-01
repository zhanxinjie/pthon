import urllib.request
import urllib.parse
# import ssl


word = input('请输入您想要搜索的内容：')

url = "http://www.baidu.com/s?"

data = {
    'ie': 'uft-8',
    'wd':'word',
}

query = urllib.parse.urlencode(data)
url = url + query

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)   Chrome/76.0.3809.100 Safari/537.36"
}

#构建请求对象
request = urllib.request.Request(url = url,headers = headers)
#发送请求
response = urllib.request.urlopen(request)

filename = word + '.html'

with open(filename, "wb") as f:
    f.write(response.read())
