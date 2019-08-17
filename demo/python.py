#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2015-10-09 13:51:35
# Project: xinwen
#http://demo.pyspider.org/debug/xinwen

from pyspider.libs.base_handler import *

import re

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.gov.cn/xinwen/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            matchObj = re.match( r'(.*).htm', each.attr.href, re.M|re.I)
            if matchObj:
                self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "http-equiv":response.doc('meta').attr('http-equiv'),
            "keywords":response.doc('meta[name="keywords"]').attr('content'),
        }
