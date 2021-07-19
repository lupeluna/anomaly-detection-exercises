import pandas as pd
import numpy as np
import os
import requests

def get_df():
    '''
    returns Lemonade data into a csv, and creates it for you
    '''
    url = "https://gist.githubusercontent.com/ryanorsinger/19bc7eccd6279661bd13307026628ace/raw/e4b5d6787015a4782f96cad6d1d62a8bdbac54c7/lemonade.csv"

    df = pd.read_csv(url)
    return df
    

    
    
    
    
    
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to create a connection urs to access database info.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    


def cache_sql_data(df, database):
    '''write dataframe to csv with title database_query.csv'''
    
    df.to_csv(f'{database}_query.csv',index = False)
        

def get_sql_data(database,query):
    ''' check if csv exists for the queried database
        if it does read from the csv
        if it does not create the csv then read from the csv  
    '''
    
    if os.path.isfile(f'{database}_query.csv') == False:   # check for the file
        
        df = pd.read_sql(query, get_connection(database))  # create file 
        
        cache_sql_data(df, database) # cache file
        
    return pd.read_csv(f'{database}_query.csv') # return contents of file



