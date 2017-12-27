
# coding: utf-8

# ### Data Explore and Analysis

# In[5]:

get_ipython().system('head *.csv')


# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
pd.options.display.mpl_style = 'default'


# In[20]:

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


# In[61]:

user_course_views_df.course_id.value_counts().plot(kind = 'bar', figsize = (10, 5))
## looks like there are some outliers. Will explore some more to find more about the outliers.


# In[41]:

course_view_counts = user_course_views_df.course_id.value_counts()
course_view_counts.head()


# In[60]:

fig, axes = plt.subplots(nrows=2, ncols=2, figsize = (20, 10))
## will create a hostogram and see how it looks like

course_view_counts.plot(kind = 'hist', ax = axes[0,0], title = "Course View Counts : Total")
course_view_counts[course_view_counts < 200].plot(kind = 'hist', ax = axes[0,1], title = "Course View Counts : < 200" )
course_view_counts[(course_view_counts > 200) & (course_view_counts < 500)].plot(kind = 'hist', title = "Course View Counts : Number of counts > 200, < 500" )
course_view_counts[course_view_counts > 500].plot(kind = 'hist', ax=axes[1,0], title = "Course View Counts : > 500")


# In[62]:

## Exploring author_handle
user_course_views_df.author_handle.nunique()


# In[66]:

authorcounts = user_course_views_df.author_handle.value_counts()
print(authorcounts[:20])
authorcounts.plot(kind = 'hist')


# In[74]:

fig, axes = plt.subplots(nrows=2, ncols=2, figsize = (20, 10))
authorcounts.plot(kind = 'hist', ax = axes[0,0], title = "Author View Counts : Total")
authorcounts[authorcounts < 200].plot(kind = 'hist', ax = axes[0,1], title = "Author View Counts : < 200" )
authorcounts[(authorcounts > 200) & (authorcounts < 500)].plot(kind = 'hist', title = "Author View Counts : Number of counts > 200, < 500" )
authorcounts[authorcounts > 500].plot(kind = 'hist', ax=axes[1,0], title = "Author View Counts : > 500")


# In[75]:

## exploring next feature "level"
levelcounts = user_course_views_df.level.value_counts()
print(levelcounts)
levelcounts.plot(kind = 'bar')

## Beginner and Intermediate has similar number of views, advanced has far less.

