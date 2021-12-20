#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np
lang = np.array(["Java","Python","PHP","JavaScript","C#","C++"])
pop = np.array([22.2,17.6,8.8,8,77,6.7])
plt.bar(lang,pop)

plt.show()


# In[8]:


plt.barh(lang,pop,color="red")
plt.show()


# In[16]:


c=["red","green","blue","orange","pink","black"]
plt.bar(lang,pop,color=c)
plt.show()


# In[ ]:




