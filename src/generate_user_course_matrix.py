from utils import *

df1 = readcsv('user_course_views.csv')
user_courses = df1[['user_handle', 'course_id']].groupby(['user_handle', 'course_id']).size().reset_index(name = 'counts')
usercoursematrix = pd.pivot_table(user_courses, values = 'counts', index = ['user_handle'], columns = 'course_id')
save_pickle(usercoursematrix, data_dir + 'usercoursematrix.pickle')
