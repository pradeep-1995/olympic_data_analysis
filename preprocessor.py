import pandas as pd

def preprocess(df,region_df):

    # filtering for summer olympic
    df = df[df['Season'] == 'Summer']
    # Merge (df,region_df)
    df = df.merge(region_df,on='NOC',how='left') 
    # Droping duplicates
    df.drop_duplicates(inplace = True)
    # One hot encoding Medal
    df = pd.concat([df,pd.get_dummies(df['Medal']).astype(int)],axis=1)

    return df
