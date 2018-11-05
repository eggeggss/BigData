#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import matplotlib.pyplot as plt

t1=[1,2,3,4]
t2=[x*2 for x in t1]


#1 上下有1個,左右有2個

plt.subplot(122,facecolor='y')
plt.plot(t1, t2, 'ro')

'''
plt.subplot(221,facecolor='k')
plt.plot(t2, t2, 'g--')

plt.subplot(223)
plt.plot(t2, t2, 'b|')
'''

""" 
plt.subplot(223,facecolor='k')
plt.plot(t2, t2, 'g--')
plt.subplot(224)
plt.plot(t2, t2, 'b|')



plt.subplot(211,facecolor='y')
plt.plot(t1, t2, 'ro')

plt.subplot(223,facecolor='k')
plt.plot(t2, t2, 'g--')
plt.subplot(224)
plt.plot(t2, t2, 'b|')
"""
"""
plt.subplot(212,facecolor='y')
plt.plot(t1, t2, 'ro')

plt.subplot(221,facecolor='k')
plt.plot(t2, t2, 'g--')

plt.subplot(222)
plt.plot(t2, t2, 'b|')

"""

# plt.subplot(121)
# plt.subplot(122)


plt.show()