from utils import *
import numpy as np
import pandas as pd
import pickle

def merge_score_matrix():
    df_tmp = pd.read_pickle('score_matrix_save8.pickle')
    df = df_tmp.iloc[0:1000]
    df_tmp = pd.read_pickle('score_matrix_save9.pickle')
    df = df.append(df_tmp.iloc[1000:2000])
    df_tmp = pd.read_pickle('score_matrix_save2.pickle')
    df = df.append(df_tmp.iloc[2000:3000])
    df_tmp = pd.read_pickle('score_matrix_save3.pickle')
    df = df.append(df_tmp.iloc[3000:4000])
    df_tmp = pd.read_pickle('score_matrix_save4.pickle')
    df = df.append(df_tmp.iloc[4000:5000])
    df_tmp = pd.read_pickle('score_matrix_save5.pickle')
    df = df.append(df_tmp.iloc[5000:6000])
    df_tmp = pd.read_pickle('score_matrix_save6.pickle')
    df = df.append(df_tmp.iloc[6000:7000])
    df_tmp = pd.read_pickle('score_matrix_save7.pickle')
    df = df.append(df_tmp.iloc[7000:8000])
    df_tmp = pd.read_pickle('score_matrix_save10.pickle')
    df = df.append(df_tmp.iloc[8000:8300])
    df_tmp = pd.read_pickle('score_matrix_save11.pickle')
    df = df.append(df_tmp.iloc[8300:8600])
    df_tmp = pd.read_pickle('score_matrix_save12.pickle')
    df = df.append(df_tmp.iloc[8600:8760])
    return df

## All split score files are copied to the current working directory
## Run the merge to generate the full score matrix

merge_score_matrix()

## The result is saved as pickle file "merged_scorematrix.pickle"
save_pickle(df, 'merged_scorematrix.pickle')



