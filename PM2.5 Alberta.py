#!/usr/bin/env python
# coding: utf-8

# #### Import libaries 

# In[87]:


import pandas as pd 
import numpy as np
import seaborn as sn 
import matplotlib.pyplot as plt 


# #### Read data into pandas 

# In[88]:


pm = pd.read_csv('PM2.5 Alberta.csv')


# #### View first 5 rows of data 

# In[89]:


pm.head()


# #### View last 5 rows of data 

# In[90]:


pm.tail()


# #### View the shape of the data 

# In[137]:


pm.shape


# #### To show the number of duplicate value present 

# In[130]:


pm.duplicated().sum()


# #### Drop duplicates in data 

# In[91]:


pm = pm.drop_duplicates()
pm


# #### Removing Null values (Nan)

# In[92]:


pm.dropna(inplace=True)
pm


# In[ ]:





# #### Dropping unnecessary columns 

# In[93]:


to_drop = ['10th Percentile', '90th Percentile']

pm.drop(to_drop, inplace=True, axis=1)


# In[94]:


pm


# #### To rename columns of the dataframe 

# In[95]:


new_name = {'Category':'Year'}

pm.rename(columns=new_name, inplace= True)


# In[96]:


pm


# #### Resetting index from 0 to 100
# 

# In[100]:


pm.reset_index(inplace=True)


# In[98]:


pm


# #### Basic information about the data 

# In[128]:


pm.info()


# #### Descriptive statistics 

# In[129]:


pm.describe()


# #### To find the number of unique values in a particular column 

# In[131]:


pm['Year'].unique()


# In[132]:


pm['Calgary'].unique()


# In[ ]:





# In[ ]:





# #### Plotting multiple lines 

# In[107]:


plt.plot(pm['Year'], pm['Calgary'], label='Calgary')
plt.plot(pm['Year'], pm['Edmonton'], label='Edmonton')
plt.plot(pm['Year'], pm['Fort McMurray'], label='Fort McMurray')
plt.plot(pm['Year'], pm['Grande Prairie'], label='Grande Prairie')
plt.plot(pm['Year'], pm['Lethbridge'], label='Lethbridge')
plt.plot(pm['Year'], pm['Medicine Hat'], label='Medicine Hat')
plt.plot(pm['Year'], pm['Red Deer'], label='Red Deer')
plt.plot(pm['Year'], pm['CAAQS'],label='CAAQS')


plt.legend()
plt.show()


# #### Drawing Bar Plots (Vertical bar)

# In[117]:


plt.bar(pm['Year'], pm['Calgary'], label='Calgary')

plt.legend()
plt.show()


# In[118]:


plt.bar(pm['Year'], pm['Edmonton'], label='Edmonton')

plt.legend()
plt.show


# #### Plotting horizontal plot

# In[119]:


plt.barh(pm['Year'], pm['Edmonton'], label='Edmonton')

plt.legend()
plt.show


# #### Scatter plots 

# In[120]:


plt.scatter(pm['Year'], pm['Calgary'])
plt.show()


# In[121]:


plt.scatter(pm['Year'], pm['Edmonton'])
plt.show()


# #### Scatter plots with a trend line or line of best fit 

# In[126]:


z = np.polyfit(pm['Year'], pm['Calgary'], 1)
p = np.poly1d(z)


plt.scatter(pm['Year'], pm['Calgary'])
plt.plot(pm['Year'], p(pm['Year']))
plt.show()


# In[146]:


pm.Calgary.describe()


# In[150]:


pm.Calgary.hist()


# In[151]:


pm.Edmonton.hist()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




