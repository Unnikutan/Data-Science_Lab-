#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x=np.array([[7,3,2],[1,2,13]])
y=np.array([[6,7,2],[1,8,9]])
print("original numbers")
print(x)
print(y)
print("Greater than Comparison : ")
print(np.greater(x,y))
print("Greater than or equal to Comparison : ")
print(np.greater_equal(x,y))
print("Less than Comparison : ")
print(np.less(x,y))
print("Less than or equal to Comparison : ")
print(np.less_equal(x,y))
