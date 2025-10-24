# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 23:47:12 2025

@author: aron-
"""
#TODO
from sklearn.datasets import fetch_covtype
import pandas as pd
import numpy as np

array = fetch_covtype(as_frame=True).frame 
# Add something here
print(array)
print(((array.columns)))