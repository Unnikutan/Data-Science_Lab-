#!/usr/bin/env python
# coding: utf-8

# In[15]:


import matplotlib.pyplot as plt
import numpy as np

lab = np.array(["G1","G2","G3","G4","G5"])
x1 = np.arange(len(lab))
y1 = np.array([22,30,35,35,26])
y2 = np.array([25,32,30,35,29])
width = 0.4
plt.bar(x1-0.2,y1,width,label="Men",color="green")
plt.bar(x1+0.2,y2,width,label="Women",color="red")
plt.xticks(x1,lab)
plt.legend()
plt.show()


# In[ ]:




