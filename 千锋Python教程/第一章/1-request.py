import urllib.request

url = "http://www.baidu.com"
#完整的url
#https://www.baidu.com:80/index.html?name=goudan&password-123#lala

response = urllib.request.urlopen(url)
# print(response.read().decode())
# print(response.getcode())
# print(response.geturl())
# print(response.getheaders())
# print(response.readlines())

with open("baidu.html", "w",encoding ='utf8') as f:
    f.write(response.read().decode())

image_url = "http://b-ssl.duitang.com/uploads/item/201808/27/20180827043223_twunu.jpg"
response = urllib.request.urlopen(image_url)
#像图片只能写入本地二进制的格式
with open("qing.jpg", "wb") as f:
    f.write(response.read())

urllib.request.urlretrieve(image_url,"chun.jpg")