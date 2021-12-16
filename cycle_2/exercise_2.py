#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
row = int(input("\n\t Enter the row size : "))
col = int(input("\n\t Enter Column Size : "))
print("\n\t enter elements of first matrix : ")
mat_1 = []
for i in range(row*col):
    mat_1.append(int(input("Enter element : ")))
array_1 = np.array(mat_1).reshape(row,col)
print("Matrix 1 : \n",array_1)
print("\n\t Enter elements of Second matrix : ")
mat_2 = []
for i in range(row*col):
    mat_2.append(int(input("Enter element : ")))
array_2 = np.array(mat_2).reshape(row,col)
print("Matrix 2 : \n",array_2)


# In[13]:


print ("\n\t Dot Product : ")
print(array_1 @ array_2)


# In[16]:


print ("\n\t Matrix 1 : \n",array_1)
print ("\n\t Transopse : \n",np.transpose(array_1))


# In[18]:


print("\n\t Trace of the matrix : ",end="")
print(np.trace(array_1))


# In[19]:


print("\n\t Rank of the Matrix : ",end="")
print(np.linalg.matrix_rank(array_1))


# In[20]:


print("\n\t Determinant of the Matrix : ",end="")
print(np.linalg.det(array_1))


# In[23]:


print("\n\t Inverse of the matrix : ")
print(np.linalg.inv(array_1))


# In[25]:


e1,e2 = np.linalg.eig(array_1)
print("\n\t Eigen values : ",e1)
print("\n\t Eigen vectors : \n",e2)