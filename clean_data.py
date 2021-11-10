import pandas as pd
import numpy as np

df = pd.read_csv("Data_Entry_2017.csv")
df.drop(columns = ['Unnamed: 11'], inplace = True)
df.head()


def subsetting(min_count = 200):
    path = "images\\"
    x = df.groupby(by = "Finding Labels")["Image Index"].count().reset_index()
    labels = list(x.loc[x["Image Index"] > min_count]["Finding Labels"])
    reduced_df = df.loc[df["Finding Labels"].isin(labels)]
    
    #removing extra No Finding rows
    reduced_df.drop(reduced_df[reduced_df["Finding Labels"] == "No Finding"].sample(frac = 0.90, random_state = 101).index, inplace = True)
    reduced_df.drop(reduced_df[reduced_df["Finding Labels"] == "Infiltration"].sample(frac = 0.40, random_state = 101).index, inplace = True)
    
    # duplicating values less than 500
    y = reduced_df.groupby(by = "Finding Labels")["Image Index"].count().reset_index()
    labels = list(y.loc[y["Image Index"] < 500]["Finding Labels"])
    reduced_df_y = df.loc[df["Finding Labels"].isin(labels)]
    final_df = reduced_df.append(reduced_df_y, ignore_index = True)
    final_df = final_df.append(reduced_df_y, ignore_index = True)
    final_df.to_csv(".", index = False)
    # add images path to imnage index
    # save dataframe
    return list(path + final_df["Finding Labels"])

def crate_subset(path_list):
    # get list of paths
    # open each image
    # resize each image to 224x224
    # save to new folder
    
    
    return