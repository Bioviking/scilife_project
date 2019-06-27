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

''' #Wrong format of dates and months
df = pd.read_table(file3, parse_dates=True, index_col='Date')
print(df.info())
print(df.head())
'''
#Parsing on the Year Month and Day Columns. To get the correct Date format.
df = pd.read_table(file3, parse_dates=[[2, 3, 4]],index_col='Year_Month_Day' ) #,parse_dates=[] index_col='Date'
#print(df.head())
print(df.info())
print(df.head())


###################################Full Dataset###############
#Removing the redunant Date column as it is not the correct format
df1 = df.iloc[:,2::]
print(df1.head())
print(df1.info())
date_ds = df1.index
print(type(date_ds))
print(date_ds)

###################################Time dataframes###############





###################################Iterating through time##############
for i in date_ds:
    i = str(i)
    i = i.split(' ')
    i = i[0] 
    print(i)
    
    
    
    
