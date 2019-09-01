import requests
import urllib
import parse
import json

url = "https://www.huya.com/cache10min.php?callback=ajaxGetHeaderAd&m=PResource&do=ajaxGetPResource&type=4&area=24&num=1"


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)   Chrome/76.0.3809.100 Safari/537.36"
}

requests = urllib.request.Request(url, headers = headers)
print(requests)

# response = requests

# response = requests.get(url = url, headers = headers)
#
# res = response.json()
#
# result = res["data"]
# print(res)

