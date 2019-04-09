#-*- coding:utf-8 -*-

import requests
url = 'http://cuijiahua.com/video/'

data = requests.get(url)
data.encoding='utf-8'

print(data.text)