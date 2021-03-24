#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as n
import pandas as p
import matplotlib.pyplot as m
data= p.read_csv("kmeans_dataset.csv")
data.drop(['Label'], axis='columns', inplace=True)
x=n.array(data)
print(x)


# In[24]:


def calc_distance(m,n):
    d=(sum((m-n)**2))**0.5
    return d
def fcc (ic,x):               #to find the closest centroid
    assigned_centroid=[]
    for i in x:
        distance=[]
        for j in ic:
            distance.append(calc_distance(i,j))
        assigned_centroid.append(n.argmin(distance))
    return assigned_centroid


# In[25]:


import random
random_sample=random.sample(range(0,len(data)),3)
random_sample


# In[26]:


centroid=[]
for i in random_sample:
    centroid.append(x[i])
centroid


# In[27]:


centroid=n.array(centroid)


# In[28]:


centroid


# In[29]:


get_centroid= fcc(centroid,x)
get_centroid


# In[30]:


for i in range(len(x)):
    if get_centroid[i]==0:
        m.scatter(x[i][0],x[i][1], color="blue")
    if get_centroid[i]==1:
        m.scatter(x[i][0],x[i][1], color="green")
    if get_centroid[i]==2:
        m.scatter(x[i][0],x[i][1], color="yellow")


# In[31]:


def clusters(gc,ds): 
    d1=[]
    d2=[]
    d3=[]
    for i in range(len(x)):
        if gc[i]==0:
            d1.append(ds[i])
        if gc[i]==1:
            d2.append(ds[i])
        if gc[i]==2:
            d3.append(ds[i])
    return n.array(d1),n.array(d2),n.array(d3)


# In[32]:


def new_centroids(gc,x):
    d1=[]
    d2=[]
    d3=[]
    for i in range(len(x)):
        if gc[i]==0:
            d1.append(x[i])
        if gc[i]==1:
            d2.append(x[i])
        if gc[i]==2:
            d3.append(x[i])
    d1=n.array(d1)
    d2=n.array(d2)
    d3=n.array(d3)
    nc=[d1.mean(axis=0),d2.mean(axis=0),d3.mean(axis=0)]
    return n.array(nc)


# In[33]:


for i in range(5):
    get_centroid=fcc(centroid,x)
    a,b,c=clusters(get_centroid,x)
    m.figure()
    m.scatter(a[:,0],a[:,1],color="blue")
    m.scatter(b[:,0],b[:,1],color="green")
    m.scatter(c[:,0],c[:,1],color="yellow")
    m.scatter(centroid[:,0],centroid[:,1],color="black")
    centroid=new_centroids(get_centroid,x)
    


# In[22]:


d1=[]
d2=[]
d3=[]
for i in range(len(x)):
    if get_centroid[i]==0:
        d1.append(x[i])
    if get_centroid[i]==1:
        d2.append(x[i])
    if get_centroid[i]==2:
        d3.append(x[i])
d1=n.array(d1)
d2=n.array(d2)
d3=n.array(d3)
nc=n.array([d1.mean(axis=0),d2.mean(axis=0),d3.mean(axis=0)])
nc


# In[120]:


nc.shape


# In[ ]:





# In[ ]:




