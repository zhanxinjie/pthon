#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 14:39
# @Author  : Xuegod Teacher For
# @File    : 01_excel_test.py
# @Software: PyCharm
import xlsxwriter


workbook = xlsxwriter.Workbook('demo.xlsx')

worksheet = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet('Python')
worksheet3 = workbook.add_worksheet("data")
worksheet4 = workbook.add_worksheet()

worksheet.set_column('A:E',20)

blod = workbook.add_format({'bold':True})

worksheet.write('A1','hello')
worksheet.write('A2','world',blod)
worksheet.write('B2','中文测试',blod)

worksheet.write(2,0,32)
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')

# worksheet.insert_image('A3','meinv.jpg')

workbook.close()