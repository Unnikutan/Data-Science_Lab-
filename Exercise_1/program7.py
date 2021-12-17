#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
array=np.arange(12).reshape(3,4)
print("Original array")
print(array)
header='col1 col2 col3'
np.savetxt('mytext.txt',array,fmt="%d",header=header)
print("After loading,the contents of the file:")
result=np.loadtxt('mytext.txt')
print(result)