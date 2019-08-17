import xlsxwriter

datas =(
        ['phone',30],
        ['tea',500]
)

workbook = xlsxwriter.Workbook('text.xlsx')
worksheet = workbook.add_worksheet('data')

bold = workbook.add_format({'bold':True})
money = workbook.add_format({'num_format':'$#.##0'})

worksheet.write('A1','Name',bold)
worksheet.write('B1','money',bold)


row,col = 1,0

for item,cost in datas:
    worksheet.write(row,col,item,bold)
    worksheet.write(row,col+1,cost,money)
    row +=1

worksheet.write(row,0,'Total',bold)
worksheet.write(row,1,'=SUM(B2:B3)',money)


workbook.close()
