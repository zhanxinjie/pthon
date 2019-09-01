import urllib.request
import urllib.parse

word = input('请输入您想要搜索的内容：')

url = "http://www.baidu.com/s?"

data = {
    'ie': 'uft-8',
    'wd':'word',
}

query = urllib.parse.urlencode(data)
url = url + query


#构建请求对象
response = urllib.request.urlopen(url = url)

filename = word + '.html'

with open(filename, "wb") as f:
    f.write(response.read())
