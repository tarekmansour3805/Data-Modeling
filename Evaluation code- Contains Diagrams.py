
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


df=pd.read_csv('plane_crashes_data.csv')


# In[6]:


df.head(1106)


# In[7]:


df.loc[df['fatalities'].idxmax()]


# In[8]:


df.groupby(['month'], sort=True)['fatalities'].sum()


# In[9]:


df.groupby(['year'])['year'].count()


# In[10]:


plt.figure(figsize=(16,9))
df.groupby(['year'])['fatalities'].count().plot();


# In[11]:


plt.figure(figsize=(16,9))
df.groupby(['year'])['fatalities'].sum().plot();


# In[12]:


plt.figure(figsize=(16,9))
df.groupby(['month'])['fatalities'].count().plot();


# In[13]:


plt.figure(figsize=(16,9))
df.groupby(['month'])['fatalities'].sum().plot();


# In[14]:


plt.figure(figsize=(16,9))
df.groupby(['month'])['fatalities'].count().plot(color='r')
df.groupby(['month'])['fatalities'].sum().plot()
plt.legend(['count','sum']);

