#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array([[5,2,3],[2,7,7],[9,6,4]])
print("array1")
print(x)
print("array2")
print(y)
print("multiplication of arrays of same size")
print(np.multiply(x,y))