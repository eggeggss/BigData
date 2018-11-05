#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import xlrd
import xlwt

read=xlrd.open_workbook('workfile.xls')
sheet=read.sheets()[0]
#sheet=read.sheets("Sheet5")
print(sheet.nrows)
print(sheet.ncols)

print(sheet.cell(5,1).value)



write = xlwt.Workbook()
write2 = write.add_sheet('MySheet')
for i in range(0,sheet.nrows):
    print(sheet.cell(i,1).value)
    value=sheet.cell(i,1).value
    write2.write(i, 0, value)
    value3=sheet.cell(i,2).value
    write2.write(i, 1, value3)

write.save('write.xls')
