#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
array=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Sum of all elemets")
print(np.sum(array))
print("Sum of each Column elements")
print(np.sum(array,0))
print("Sum of each row elements")
print(np.sum(array,1))
