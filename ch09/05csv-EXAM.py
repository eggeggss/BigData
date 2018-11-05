#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"
import csv
sum=0
with open('wordfile2.csv', 'r',encoding='utf8') as fin:
    with open('write.csv', 'w',encoding='utf8') as fout:
        read = csv.reader(fin, delimiter=',')
        write = csv.writer(fout, delimiter=',')
        header = next(read)
        print(header)
        first_item = header[0]
        write.writerow(header)
        for row in read:
            print(','.join(row))
            write.writerow(row)
            print(row[4])
            t1=row[4]
            t1=t1.replace(",","")
            t1=int(t1)
            sum=sum+t1

print("sum=%d" % sum)
print("sum=",sum)