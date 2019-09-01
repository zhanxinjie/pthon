import urllib.parse

# url只能由特定的字符组成：字母、数字、下划线
# 如果出现其他的，如$ 空格 中文等，就要对其进行编码

url = "http://baidu.com/index.html?name=好人&pwd=123456"

ret = urllib.parse.quote(url)
print(ret)

re = urllib.parse.unquote(url)
print(re)