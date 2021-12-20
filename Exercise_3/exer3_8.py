#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import numpy as np

lang = np.array(["Java","Python","PHP","JavaScript","C#","C++"])
pop = np.array([22.2,17.6,8.8,8,77,6.7])
plt.pie(pop,labels=lang)

plt.show()

