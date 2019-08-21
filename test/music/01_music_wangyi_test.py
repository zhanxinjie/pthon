#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 14:55
# @Author  : Xuegod Teacher For
# @File    : 01_music_wangyi_test.py
# @Software: PyCharm
import requests#pip install requests
import urllib.request
import re
def get_response(url,headers):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response
        return None
    except:
        return None

def get_song_name(songid):
    '''
    :param songid: 歌曲id
    :return: 歌曲名字
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    url = 'https://music.163.com/song?id={}'.format(songid)
    Text = get_response(url,headers).text
    #re正则匹配 .任意字符，*重复前面字符的0次或者是无线多次，
    title = re.findall('<title>(.*?)</title>',Text,re.S)
    name = title[0].split('-')[0]
    return name.strip()

if __name__ == '__main__':
    songid = input('请输入歌曲的id:')
    # name = get_song_name(412911436)
    url = 'http://music.163.com/song/media/outer/url?id={}'.format(songid)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    down_url =  get_response(url,headers).url

    song_name = get_song_name(songid)
    #这是把网上的数据 下载到本地，第一个参数 url 第二个参数本间文件名
    urllib.request.urlretrieve(down_url,song_name+'.mp3')
