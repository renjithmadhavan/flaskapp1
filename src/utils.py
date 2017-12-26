import pandas as pd
import numpy as np
from datetime import datetime
import pickle
import sys

data_dir="C:\\renjith\\projects\\data\\"

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

def load_pickle(filename):
    with open(filename, 'rb') as f:
        content = pickle.load(f)
    return content

def find_similar_users(userid, N):
    similar_df = pd.read_pickle(data_dir + 'similar_df_master.pickle')
    top_n_users = similar_df.loc[userid][:N]
    return top_n_users
