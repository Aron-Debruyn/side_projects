# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 23:47:12 2025

@author: aron-
"""

from sklearn.datasets import fetch_covtype
import pandas as pd
 
# Get the dataset
df = pd.DataFrame(fetch_covtype(as_frame=True))
 
# Print the first 5 rows of the dataframe
print(df.head())