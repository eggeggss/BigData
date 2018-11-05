#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt
t=[1,2,3,4]
plt.plot(t, t, 'r--')
plt.plot( t, [x*2 for x in t], 'bs')
plt.plot( t, [x*3 for x in t], 'g^')
plt.plot( t, [x*4 for x in t], 'k:')
plt.show()