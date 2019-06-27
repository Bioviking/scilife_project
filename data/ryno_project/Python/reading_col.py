# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:21:53 2017

@author: Bioviking
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file1 = '../data/ryno_project/P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv'
file2 = '../data/ryno_project/AF2-SCG present in each bin.tsv'
file3 = '../data/ryno_project/LMO_time_series_Metadata_to_Barbel_mod.txt'
file4 = '../data/ryno_project/reference_genomes.xlsx'

idfile1 = '../data/ryno_project/LMO.indiv.MAGs.merged.COG.tsv'
idfile2 = '../data/ryno_project/LMO.indiv.MAGs.merged.EC.tsv'
idfile3 = '../data/ryno_project/LMO.indiv.MAGs.merged.PFAM.tsv'
idfile4 = '../data/ryno_project/LMO.indiv.MAGs.merged.TIGRFAM.tsv'

#################Head of the whole of file1#################
print(str(file1))
df= pd.read_table(file1)
print(df.head())

#################Head of the whole of file2#################
print(str(file2))
df= pd.read_table(file2)
print(df.head())

#################Head of the whole of file3#################
print(str(file3))
df= pd.read_table(file3)
print(df.head())

#################ExcelFile Head of the whole of file4#################
print(str(file4))
xl= pd.ExcelFile(file4)
print(xl.sheet_names)

#################Head of the whole of idfile1#################
print(str(idfile1))
df= pd.read_table(idfile1)
print(df.head())

#################Head of the whole of idfile2#################
print(str(idfile2))
df= pd.read_table(idfile2)
print(df.head())

#################Head of the whole of idfile3#################
print(str(idfile3))
df= pd.read_table(idfile3)
print(df.head())

#################Head of the whole of idfile4#################
print(str(idfile4))
df= pd.read_table(idfile4)
print(df.head())

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return(langs_count)




# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)