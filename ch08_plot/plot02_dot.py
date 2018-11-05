#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
#plt.plot([1,2,3,4], [1,4,9,16],'b' )
plt.plot([1,2,3,4], [1,4,9,16], 'ro')#r => 顏色 o=>圓標記
#plt.plot([1,2,3,4], [1,4.5,9.5,16.5], 'g')
plt.axis([0, 6, 0, 20])# x: 0~6  y:0~10
plt.ylabel('some numbers')
plt.xlabel('times')
plt.show()