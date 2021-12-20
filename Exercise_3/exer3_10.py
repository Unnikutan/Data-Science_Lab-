#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np

math = np.array([88,92,80,89,100,80,60,100,80,34])
science = np.array([35,79,79,48,100,88,32,45,20,30])
rang = np.array([10,20,30,40,50,60,70,80,90,100])

plt.scatter(rang,math,label="Maths")
plt.scatter(rang,science,label="Science")
plt.xlabel("Mark Range")
plt.ylabel("Mark Scored")
plt.title("Scatter Plot")
plt.legend()
plt.show()


# In[ ]:




