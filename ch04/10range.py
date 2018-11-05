#!/usr/bin/env
a=range(10)
print(a)         # Pyton 2.x
print(list(a))   # Pyton 3.x
print(a[2])
'''
for i in [x * 0.1 for x in range(6,0,-2)]:
    print (i)
'''

for x in range(1,10):
    for y in range(1,10):
        print("{} x {} = {}".format(x,y,x*y))