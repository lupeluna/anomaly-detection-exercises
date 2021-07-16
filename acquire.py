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
    
    



