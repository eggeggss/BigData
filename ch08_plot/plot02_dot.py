#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16] )
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.plot([1,2,3,4], [1,4.5,9.5,16.5], 'b-')
plt.axis([0, 6, 0, 20])
plt.ylabel('some numbers')
plt.xlabel('times')
plt.show()