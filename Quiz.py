#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:



arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[73]:


arr[arr%2==1]  #extracting odd numbers


# In[93]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_val = arr[arr%2==1]  #replacing odd values with -1
arr[odd_val] = -1
arr


# In[13]:


arr = np.arange(10)         #1D to 2D array with 2 rows
np.reshape(arr,(2,-1))


# In[14]:


a = np.arange(10).reshape(2,-1) #vertical stack
b = np.arange(10).reshape(2,-1)


# In[16]:


np.vstack((a,b))


# In[95]:


a = np.array([2, 6, 1, 9, 10, 3, 27])
val = a[(a>5)*(a<=10)]          # between 5 and 10
val


# In[18]:


a = np.array([2, 6, 1, 9, 10, 3, 27])


# In[31]:


a[a>5],a[a<=10] #need to find orginal


# In[34]:


av = np.arange(10,50)   #vector with 10 to 49


# In[35]:


av


# In[45]:


ar = np.random.rand(10,10) #min & max value


# In[46]:


ar.min()


# In[41]:


ar.max()


# In[48]:


matrix = np.array([[1,2,3],
                  [4,5,6],    #transpose matrix
                  [7,8,9]])


# In[49]:


np.transpose(matrix)


# In[52]:


arr1 = np.array([[2,3],
                [5,6]])
arr2 = np.array([[7,8],
                [9,10]])    #Dot product


# In[53]:


np.dot(arr1,arr2)


# In[59]:


np.random.seed(100)
a = np.random.randint(1,10, [5,3])  #max in each row
a.max(axis=1)


# In[62]:


data = np.random.randint(10,100,(5,4))#3rd&5th row and 3rd&4th col
data[[2,4],2:4]


# In[63]:


matrix = np.array([[1,2,3],
          [4,5,6],
          [7,8,9]])


# In[68]:


m = matrix.flatten()    #matrix to vector
m


# In[69]:


m = np.array([[2,3],
              [2,4]])


# In[70]:



np.linalg.inv(m)


# In[71]:


ma = np.random.rand(3,3) matrix from a uniform distribution


# In[72]:


ma


# In[ ]:




