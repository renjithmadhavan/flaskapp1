#!/home/renjith/anaconda3/bin/python
import pandas as pd
import numpy as np
from datetime import datetime
import pickle
import sys

def find_similar_users(userid, number_show):
    # Function to find similar users
    return results

def readcsv(filename):
    df = pd.read_csv(filename)
    return df

def similarity(user1, user2):
    user1 = np.array(user1)
    user2 = np.array(user2) 
    commoncourses = [i for i in range(len(user1)) if user1[i] > 0 and user2[i] > 0]
    return len(commoncourses)

def save_pickle(obname, filename):
    pickle.dump(obname, open(filename, "wb"))
    return 0

df1 = readcsv('user_course_views.csv')
user_courses = df1[['user_handle', 'course_id']].groupby(['user_handle', 'course_id']).size().reset_index(name = 'counts')
print(user_courses.head())

usercoursematrix = pd.pivot_table(user_courses, values = 'counts', index = ['user_handle'], columns = 'course_id')

score_matrix = pd.DataFrame(index = usercoursematrix.index, columns = usercoursematrix.index)
score_matrix = score_matrix.fillna(0)  

print(str(datetime.now()))
#for i in range(len(score_matrix.index)):
for i in range(2000):
    print(i)
    #if i%200 == 0:
     #   print(i)
    currentuserid = score_matrix.index[i]
    current_user = usercoursematrix.loc[currentuserid]
    for j in range(len(score_matrix.index)):
    #for j in range(1000):
        #print(currentuserid)
        #print(compareuserid)
        #print(j)
        compareuserid = score_matrix.index[j]
        compare_user = usercoursematrix.loc[compareuserid]
        #print(current_user)
        #print(compare_user)
        score_matrix.iloc[i, j] = similarity(current_user, compare_user)
save_pickle(score_matrix, "score_matrix_save1.pickle")
print(str(datetime.now()))
