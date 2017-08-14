# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:36:55 2017

file3_processor.py

@author: Bioviking
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file3 = '../LMO_time_series_Metadata_to_Barbel_mod.txt' #input('Please enter the file name:')

df = pd.read_table(file3, parse_dates=True, index_col='Date')

#Remove other Date & time columns


print(df.head())