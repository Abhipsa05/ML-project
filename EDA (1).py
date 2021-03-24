#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as n
import pandas as p
import matplotlib.pyplot as m
data= p.read_csv("kmeans_dataset.csv")
x=n.array(data)
print(data)


# In[3]:


X=[]
Y=[]
for i in range(len(x)):
    X.append(x[i][0])
    Y.append(x[i][1])


# In[4]:


m.scatter(Y,X)
m.show()


# In[5]:


data.describe()


# In[6]:


data.info()


# In[11]:


label =['Tier A','Tier B','Tier c','Tier D']
people=[38,203,110,109]
m.pie(people,labels=label,autopct='%0.2f%%')
m.show()


# In[ ]:




