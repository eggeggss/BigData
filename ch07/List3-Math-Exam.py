#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
list1 = [59,60,70,80]
list1=[x+10 for x in list1 if x>=60]
print(list1)

list1=[1,1,2,2,3,3]
list1.remove(2)
print(list1)

list1=[1,1,2,2,3,3]
#for x in list1:
#  print(list1)
#  x=x

x=0
while x<len(list1):
    list1.remove(2)
    x=x+1



"""
x = [1,2,3,2,2,2,3,4]
list(filter(lambda a: a != 2, x))
print(x)
"""
