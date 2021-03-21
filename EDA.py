#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as n
import pandas as p
import matplotlib.pyplot as m
data= p.read_csv("kmeans_dataset.csv")
x=n.array(data)
print(data)


# In[4]:


X=[]
Y=[]
for i in range(len(x)):
    X.append(x[i][0])
    Y.append(x[i][1])


# In[5]:


m.scatter(Y,X)
m.show()


# In[6]:


data.describe()


# In[7]:


data.info()


# In[ ]:




