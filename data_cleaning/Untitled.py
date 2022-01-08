#!/usr/bin/env python
# coding: utf-8

# In[234]:


import pandas as pd
import numpy as np


# In[235]:


file_path = "TICKERS.csv"


# In[236]:


tickers = pd.read_csv(file_path)
tickers.head()


# In[237]:


tickers.dtypes


# In[238]:


tickers.shape


# In[239]:


usage_by_col = tickers.memory_usage(deep=True) # returns memory usage for each column
total_usage = usage_by_col.sum()
mbs = total_usage / 1e6 # convert to megabytes 
mbs


# In[240]:


tickers.isnull().any()


# In[241]:


print(type(tickers))


# In[242]:


tickers.drop_duplicates(subset ="ticker", keep = 'first', inplace = True)


# In[243]:


tickers.drop(['cusips', 'siccode','sicsector', 'sicindustry', 'famasector', 'famaindustry', 'currency'] , inplace=True, axis=1)


# In[244]:


tickers.drop(tickers.index[tickers['isdelisted'] == 'Y'], inplace=True)


# In[245]:


tickers.head()


# In[246]:


no_na_tickers = tickers.dropna(subset=['ticker', 'scalemarketcap'])


# In[247]:


no_na_tickers.isnull().any()


# In[248]:


print(no_na_tickers['scalemarketcap'].unique())


# In[ ]:





# In[249]:


print(no_na_tickers['isdelisted'].unique())


# In[250]:


no_na_tickers['scalemarketcap'].describe()


# In[251]:


no_na_tickers.describe()


# In[252]:


no_na_tickers['ticker'].describe()


# In[253]:


no_na_tickers['sector'].describe()


# In[254]:


no_na_tickers['industry'].describe()


# In[ ]:





# In[255]:


no_na_tickers['ticker'].describe()


# In[256]:


no_na_tickers.head(50)


# In[ ]:





# In[257]:


no_na_tickers.head(50)


# In[258]:


no_na_tickers.isnull().any()


# In[259]:


no_na_tickers['industry'].describe()


# In[260]:


usage_by_col = no_na_tickers.memory_usage(deep=True) # returns memory usage for each column
total_usage = usage_by_col.sum()
mbs = total_usage / 1e6 # convert to megabytes 
mbs


# In[261]:


no_na_tickers.shape


# In[263]:


no_na_tickers.to_excel("cleaned_tickers1.xlsx")


# In[ ]:





# In[ ]:




