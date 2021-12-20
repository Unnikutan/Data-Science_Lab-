#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1,2,3,4])
y1 = np.array([2,4,6,8])
plt.subplot(2,2,1)
plt.plot(x,y)

x2 = np.array([1,3,5,7])
y2 = np.array([4,8,2,1])
plt.subplot(2,2,2)
plt.plot(x2,y2)

x3 = np.array([3,6,9,12])
y3 = np.array([6,5,1,9])
plt.subplot(2,2,3)
plt.plot(x3,y3)

x4 = np.array([1,9,1,3])
y4 = np.array([2,5,10,13])
plt.subplot(2,2,4)
plt.plot(x4,y4)

plt.show()


# In[ ]:




