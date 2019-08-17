#-*— coding:utf-8 -*-
#pip install baidu-aip
#pip install config

_author_='Zhanxinjie'

'''
    功能：利用百度官方api，读取图片中的文字，同时将文字转成语音
    官方地址：http://console.bce.baidu.com/ai/?fromai=1#/ai/ocr/overview/index
'''

import config
from aip import AipOcr,AipSpeech

import cv2

""" 自己的APPID AK SK """
##APP_ID = config.baidu_app_id
##API_KEY = config.baidu_api_key
##SECRET_KEY = config.baidu_secret_key

APP_ID = '15350589'
API_KEY = 'aSAW4VO8n33r13wxe5L6qOEH'
SECRET_KEY = 'DlZs6G6HDNl8IU8gGrXVlwIxbEPlgxH2'

clientAipOcr = AipOcr(APP_ID,API_KEY,SECRET_KEY)
clientAipSpeech = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

#测试图片
picture_url="http://image.bug2048.com/mongo20180906.jpg"

fname = 'picture/test4.jpg' 

"""读取图片"""
def get_file_conten(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
    
image = get_file_conten(fname)

"""调用通用文字识别，图片参数为本地图片"""
results = clientAipOcr.general(image)["words_result"]

img =cv2.imread(fname)
for result in results:
    text =result["words"]
    location = result["location"]

    print(text)
    #画矩形框
    cv2.rectangle(img,(location["left"],location["top"]),(location["left"]+location["width"],location["top"]+location["height"]),(0,255,0),2)

cv2.imwrite(fname[:-4]+"_result.jpg",img)

"""
    1.调用文字识别API识别图片上的文字
    2.拼接文字后调用语音合成API转成语音
"""


def convert_picture_words():
    words=''
    wordsResult=clientAipOcr.basicGeneralUrl(picture_url)
    for item in wordsResult['words_result']:
        words+=item['words']+','
    if words=='':
        resturn
    words=words[:-1]
    print(words)
    speechResult=clientAipSpeech.synthesis(words,'zh',1,{
        'vol':5,
        'per':3
        })

    #识别正确返回语音二进制，错误则返回dict 参数下面错误码
    if not isinstance(speechResult,dict):
        with open('result.mp3','wb') as f:
            f.write(speechResult)



if __name__ == '__main__':
    convert_picture_words()
     
