#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
def fun3(num1=0,num2=0):
    return (num1*2)+num2

def fun4():
    return 1,2

a=fun3(1,2)
print(a)
a=fun3(num1=1,num2=2)
print(a)
a=fun3(num2=1,num1=2)
print(a)
a=fun3(num2=1)
print(a)
a=fun3()
print(a)
a,b=fun4()
print(a)
print(b)




