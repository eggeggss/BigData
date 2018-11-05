#!/usr/bin/env python
# author: Powen Ko      www.powenko.com
import matplotlib.pyplot as plt

# y=x/0.3+0
plt.plot([0,1,2], [0,0.3,0.6], 'gx')
plt.plot([0,1,2], [0,0.3,0.6], 'r--')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()