import pandas as pd
import numpy as np
import os
import requests
from acquire import get_df




df = get_df()
df.head()

def get_upper_and_lower_bounds(col, mult=1.5):
    '''
    positional argument: col, a pandas Series
    kwarg: mult: float value representing multiplier in tukey IQR boundaries
    
    return: lower_bound, upper_bound, two float values representing the fence values of our IQR based boundaries
    '''
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - iqr * mult
    upper_bound = q3 + iqr * mult
    return lower_bound, upper_bound





# at a multiplier of 1.5:
outliers = {}
for col in df.columns:
    if np.issubdtype(df[col].dtype, np.number):
        lower_bound, upper_bound = get_upper_and_lower_bounds(df[col])
        print(f' Lower bound for {col} : {lower_bound}\n Upper bound for {col}: {upper_bound}\n')
        print('-----------------\n')
        outliers[col] = {}
        outliers[col]['bounds'] = {'upper': upper_bound, 'lower': lower_bound}
        outliers[col]['df'] = df[(df[col] > upper_bound) | (df[col] < lower_bound)]
    else:
        pass
    
    

    
    



# # This function will take in an entire dataframe, and operate on a lit of columns...
# def get_low_and_up_bounds_df(df, k=1.5):
#     '''
#     This function takes in a pandas dataframe, list of columns, and k value, and will print out upper and lower bounds for each column.
#     It takes in a default argument of the col_list being all numeric columns, and the k value=1.5
#     '''
#     col_list=list(df.select_dtypes(include=['int', 'float'], exclude='O'))
#     for col in col_list:
#         # Find the lower and upper quartiles
#         q_25, q_75 = df[col].quantile([0.25, 0.75])
#         # Find the Inner Quartile Range
#         q_iqr = q_75 - q_25
#         # Find the Upper Bound
#         q_upper = q_75 + (k * q_iqr)
#         # Find the Lower Bound
#         q_lower = q_25 - (k * q_iqr)
#         # Identify outliers
#         outliers_lower = df[df[col] < q_lower]
#         outliers_upper = df[df[col] > q_upper]
#         outliers_all = pd.concat([outliers_lower, outliers_upper], axis=0)
#         print('')
#         print(col)
#         print(f'K: {k}')
#         print(f'Lower Fence: {q_lower}')
#         print(f'Upper Fence: {q_upper}')
#         print('')
#         print(f'Lower Outliers in {col}')
#         print('')
#         print(outliers_lower)
#         print('')
#         print(f'Upper Outliers in {col}')
#         print('')
#         print(outliers_upper)
#         print('')
#         print(f'All Outliers in {col}')
#         print('')
#         print(outliers_all)
#         plt.figure(figsize=(16,4))
#         plt.subplot(1, 2, 1)
#         sns.histplot(data = df, x = col, kde=True)
#         plt.title(col)
#         plt.subplot(1, 2, 2)
#         sns.boxplot(x=col, data=df)
#         plt.title(col)
#         plt.show()
#         print('-------------------------------------------------------------------')
        
        
        
        
        
        
        
        
        
# Function to get the zscores
def z_score_func(df):
    col_list= ["Temperature", "Rainfall", "Flyers", "Sales"]
    for col in col_list:
        z_score = pd.Series((df[col]-df[col].mean())/ df[col].std())
        z_score_name = str(col) + '_zscore'
        df[z_score_name] = z_score
        return df
    
    
    
    
    
    
def z_score_func(df, n1, n2):
    '''
    This function reads in dataframe, the first standard deviation, the second deviation, and outputs
    a list of columns within the first standard deviation set and the second standard deviation set for each column
    '''
    col_list= ["Temperature", "Rainfall", "Flyers", "Price", "Sales"]
    for col in df[col_list]:
        # Calculate the z-score 
        zscores = pd.Series((df[col] - df[col].mean()) / df[col].std())
        # Finds all of the observations two standard deviations or more.
        standard_dev2= df[df[col].abs() >= n1]
        # Finds all of the observations three standard deviations or more
        standard_dev3= df[df[col].abs() >= n2]
        print('-------------------------------------------------------------------------------------------- \n \n')
        print(f'Standard Deviation 2 of {col}')
        print(standard_dev2)
        print('-------------------------------------------------------------------------------------------- \n \n')
        print(f'Standard Deviation 3 {col}')
        print(standard_dev3) 