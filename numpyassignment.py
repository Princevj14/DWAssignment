#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[ ]:


1. Create a null vector of size 10 but the fifth value which is 1.


# In[27]:


b = np.zeros(10) 
b[4] = 1
print(b)


# In[ ]:


2. Create a vector with values ranging from 10 to 49.


# In[5]:


a = np.arange(10,50) 
print(a)


# In[ ]:





# In[ ]:


3. Create a 3x3 matrix with values ranging from 0 to 8


# In[7]:


x = np.arange(0,9).reshape(3,3)
print(x)


# In[ ]:


4. Find indices of non-zero elements from [1,2,0,0,4,0]


# In[12]:


y  = np.array([1,2,0,0,4,0])
z = np.nonzero(y)
print(z)


# In[ ]:


5. Create a 10x10 array with random values and find the minimum and maximum values.


# In[20]:



a = np.random.rand(10,10)
a.min()


# In[21]:


a.max()


# In[ ]:


6. Create a random vector of size 30 and find the mean value.


# In[22]:


v = np.arange(31)


# In[23]:


v.mean()


# In[24]:


v


# In[ ]:




