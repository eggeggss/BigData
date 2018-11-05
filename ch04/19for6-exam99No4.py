#!/usr/bin/env
# -*- coding:utf-8  -*-

for x in range(1,10):
    for y in range(1,10):
        if x==4 or y==4:
          print("")
        else:
          print(" %d*%d=%d" % ( x,y,x*y))

print("end")
