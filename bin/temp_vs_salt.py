# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:28:28 2017

@author: Admin
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file3 = '../data/ryno_project/LMO_time_series_Metadata_to_Barbel_mod.txt'


#Parsing on the Year Month and Day Columns. To get the correct Date format.
df = pd.read_table(file3, parse_dates=[[2, 3, 4]],index_col='Year_Month_Day' ) #,parse_dates=[] index_col='Date'
#print(df.head())
print(df.info())



###################################Full Dataset###############
#Removing the redunant Date column as it is not the correct format
df1 = df.iloc[:,2::]
print(df1.head(50))
print(df1.info())


#####################Temperature and salinity#####################

sns.lmplot(x='Salinity', y='Temperature', data=df1)

plt.show()
plt.clr


df1.plot([['Nitrate'], ['Phosphate']], kind= 'line')

plt.show()
plt.clr

#sns.pairplot(df1)