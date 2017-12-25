from utils import *
import pandas as pd
import numpy as np

## load the score matrix using pickle read

tmp = pd.read_pickle('merged_scorematrix.pickle')


## below function will find the user'ids for each score and create a final matrix in descending order.
## The index of the matrix is userid.

def similar_users_matrix():
    merged_df = pd.read_pickle('merged_scorematrix.pickle')
    tmp = np.flip(merged_df.values.argsort(), 1)
    similar_df = pd.DataFrame.from_records(merged_df.columns[tmp], index = merged_df.index)
    return similar_df


similar_df = similar_users_matrix()
# save the similar user matrix as a pickle file
save_pickle(similar_df, 'similar_df_master.pickle')

