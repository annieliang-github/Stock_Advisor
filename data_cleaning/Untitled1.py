#!/usr/bin/env python
# coding: utf-8

# In[96]:


import pandas as pd
import numpy as np


# In[107]:


file_path = "DAILY.csv"
clean_path = "cleaned_tickers1.xlsx"


# In[108]:


tickers = pd.read_csv(file_path)
tickers.head()


# In[109]:


clean = pd.read_excel(clean_path)
clean.head()


# In[110]:


tickers.isnull().any()


# In[111]:


clean_set = set(clean['ticker'])
print(clean_set)


# In[112]:


len(tickers['ticker'].unique())


# In[114]:


extra = set(tickers['ticker'].unique()) - clean_set 
print(extra)


# In[115]:



# tickers["ticker"] = tickers["ticker"].astype("|S")


# In[116]:


# tickers.head(30)


# In[117]:


# tickers.drop(tickers[tickers['ticker'] in extra].index, inplace = True)


# In[118]:


# tickers['ticker'] in extra


# In[119]:


test = tickers[tickers["ticker"].isin(clean_set)]


# In[120]:


test.head(500)


# In[81]:





# In[121]:


len(test['ticker'].unique())


# In[122]:


test.to_csv("cleaned_DAILY.csv")


# In[ ]:




