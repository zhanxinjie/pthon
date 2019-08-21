#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 21:28
# @Author  : Xuegod Teacher For
# @File    : 03_tesseract_test.py
# @Software: PyCharm
import pytesseract # tesseract-ocr
from PIL import Image # pip install pillow

img = Image.open('2.png')

result = pytesseract.image_to_string(img)

print(result)
