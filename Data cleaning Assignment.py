#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis',  'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', ' (12)', '(British Airways. )', '12. Air France', '"Swiss Air"']})


# In[2]:


df


# In[3]:


df['FlightNumber'].fillna(value=df['FlightNumber'][0]+10, limit=1, inplace=True)
df['FlightNumber'].fillna(value=df['FlightNumber'][2]+10, limit=1, inplace=True)


# In[4]:


df


# In[5]:


df['FlightNumber'].dtype


# In[6]:


df['FlightNumber'] = df['FlightNumber'].astype(np.int64)
df['FlightNumber'].dtype


# In[7]:


df


# In[8]:


temp_data = pd.DataFrame(df['From_To'].str.split('_', 1).to_list(), columns = ['From','To'])
temp_data


# In[9]:


temp_data['From'] = temp_data['From'].str.capitalize()
temp_data['To'] = temp_data['To'].str.capitalize()


# In[10]:


temp_data


# In[11]:


df = pd.concat([temp_data, df], axis=1, sort=False)
df


# In[12]:


delays = pd.DataFrame(df['RecentDelays'].to_list(), columns = ['delay_1', 'delay_2', 'delay_3'])
delays


# In[13]:


df.drop(['RecentDelays'], inplace=True, axis=1)
df


# In[14]:


df.insert(loc = 3, column='delay_1' , value=delays['delay_1'])
df.insert(loc = 4, column='delay_2' , value=delays['delay_2'])
df.insert(loc = 5, column='delay_3' , value=delays['delay_3'])
df


# In[ ]:




