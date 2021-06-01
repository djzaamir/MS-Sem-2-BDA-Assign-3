#!/usr/bin/env python
# coding: utf-8

# In[25]:


#libraries
import pandas as pd
from sklearn.cluster import KMeans


# In[2]:


#dataset
df=pd.read_csv('pokec.csv', delimiter = "\t")


# In[3]:


df


# In[26]:


#check nulls from the 
df.isnull().sum()


# In[5]:


#drop the column with more than 70% nulls
df.drop(axis=1, columns='life_style', inplace=True)


# In[6]:


#dropping all nulls from the dataset
toy=df.dropna()


# In[7]:


toy


# In[9]:


toy.columns


# In[8]:


#to check for the numerical columns for the kmeans clustering 
toy.info()


# In[13]:


#columns for the kmnean
cols=['user_id','AGE','Height','Weight','BMI']


# In[20]:


#taking first 30000 user for training data
cluster=toy[cols].iloc[0:29999]
cluster=cluster.set_index('user_id') 


# In[21]:


cluster


# In[23]:


#Kmeans clustering 
kmeans = KMeans(n_clusters=5,verbose=1) # You want cluster the passenger records into 2: Survived or Not survived
kmeans.fit(cluster)


# In[24]:


#cluster centroids
print(kmeans.cluster_centers_)


# In[ ]:




