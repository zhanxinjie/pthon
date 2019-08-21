#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 15:06
# @Author  : Xuegod Teacher For
# @File    : 02_chart_test.py
# @Software: PyCharm
import xlsxwriter
workbook = xlsxwriter.Workbook('chart.xlsx')

worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type':'column'})
for i in range(2,5):
    chart.add_series({
        'categories':'=Sheet1!$A$1:$G$1',
        'values':'=Sheet1!$A$%s:$G$%s'%(i,i),
        'line':{'color':'black'}
    })

data = [
    ['星期一','星期二','星期三','星期四','星期五','星期六','星期日'],
    [150,152,158,149,155,145,148],
    [89, 88,95,93, 98,100, 99],
    [201,200,198,175,170,198,195],
]
worksheet.write_row('A1',data[0])
worksheet.write_row('A2',data[1])
worksheet.write_row('A3',data[2])
worksheet.write_row('A4',data[3])

chart.set_x_axis({
    'name':'for Test',
    'name_font':{'size':14,'blod':True},
    'num_font':{'italic':True}
})
chart.set_size({'width':577,'height':287})
chart.set_title({'name':'业务报表'})
chart.set_y_axis({'name':'Mb/s'})


worksheet.insert_chart('A5',chart)

workbook.close()