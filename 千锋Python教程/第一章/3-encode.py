import urllib.parse

url = "http://www.baidu.com/index.html"
# url = "http://www.baidu.com/index.html?name=goudan&age=18&sex=nv&height=180"
#假如参数有name age sex height
data ={
    'name':'name',
    'age':'age',
    'sex':'sex',
    'height':'height',
}
query_string = urllib.parse.urlencode(data)
print(query_string)

# 遍历字典
# lt = []
# for k,v in data.items():
#     lt.append(k + '=' + str(v))
# query_string = '&'.join(lt)

url = url + '?' + query_string
print(url)