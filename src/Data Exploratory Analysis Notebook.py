
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


# In[2]:

user_interests_df = pd.read_csv("user_interests.csv")


# In[8]:

user_interests_df[user_interests_df.user_handle == 8035]


# In[9]:

user_interests_df[user_interests_df.user_handle == 7200]


# In[10]:

get_ipython().system('ls -ltr ../../data')


# In[17]:

df1 = pd.read_pickle('../../data/similar_df_master.pickle')


# In[29]:

df1.loc[1234]


# In[28]:

user_course_views_df[user_course_views_df.user_handle == 1234]


# In[27]:

user_course_views_df[user_course_views_df.user_handle == 6092]


# In[30]:

from utils import *


# In[92]:

df1 = readcsv('user_course_views.csv')


# In[54]:

user_courses = df1[['user_handle', 'course_id']].groupby(['user_handle', 'course_id']).size().reset_index(name = 'counts')
usercoursematrix = pd.pivot_table(user_courses, values = 'counts', index = ['user_handle'], columns = 'course_id')


# In[55]:

current_user = usercoursematrix.loc[1234]


# In[56]:

compare_user = usercoursematrix.loc[6092]


# In[51]:

def similarity(user1, user2):
    user1 = np.array(user1)
    user2 = np.array(user2) 
    commoncourses = [i for i in range(len(user1)) if user1[i] > 0 and user2[i] > 0]
    return len(commoncourses)


# In[58]:

#current_user


# In[ ]:




# In[59]:

similarity(current_user, compare_user )


# In[61]:

current_user[1:10]


# In[62]:

compare_user[1:10]


# In[63]:

merged_df = pd.read_pickle(data_dir + 'merged_scorematrix.pickle')


# In[65]:

merged_df.loc[12].values.argsort()


# In[84]:

merged_df = pd.read_pickle(data_dir + 'merged_scorematrix.pickle')


# In[85]:

tmp = np.flip(merged_df.values.argsort(), 1)


# In[86]:

similar_df = pd.DataFrame.from_records(merged_df.columns[tmp], index = merged_df.index)


# In[72]:

from utils import *


# In[74]:

get_ipython().magic('pinfo2 find_similarity_score')


# In[81]:

importlib.reload(sys.modules['utils'])


# In[82]:

from utils import *


# In[96]:

find_similarity_score(12, 1011)


# In[88]:

similar_df.loc[12][:10]


# In[93]:

df1[df1.user_handle == 7580]


# In[95]:

df1[df1.course_id == "java-patterns-concurrency-multi-threading"]


# In[114]:

def find_common_courses(user1, user2):
    user_course_df = pd.read_pickle(data_dir + 'usercoursematrix.pickle')
    user1 = user_course_df.loc[user1]
    user2 = user_course_df.loc[user2]
    commoncourses = [user_course_df.columns[i] for i in range(len(user1)) if user1[i] > 0 and user2[i] > 0]
    return commoncourses


# In[112]:

user_course_df.columns[2802]
user1.columns


# In[ ]:



