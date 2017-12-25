
# coding: utf-8

# ### Data Explore and Analysis

# In[5]:

get_ipython().system('head *.csv')


# In[25]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[9]:

user_course_views_df = pd.read_csv('user_course_views.csv')
print(user_course_views_df.shape)


# In[10]:

user_course_views_df.head()


# In[16]:

user_course_views_df.describe()


# In[12]:

## Total number of users
user_course_views_df.user_handle.nunique()


# In[18]:

print(user_course_views_df.view_date.min())
print(user_course_views_df.view_date.max())
## So the data is of 5 Months


# In[19]:

## How many courses are viewed
user_course_views_df.course_id.nunique()


# In[ ]:

user_course_views_df.course_id.value_counts().plot(kind = 'bar', figsize = (20, 10))


# In[ ]:



