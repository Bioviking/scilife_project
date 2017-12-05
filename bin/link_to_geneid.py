# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:11:06 2017

@author: Bioviking

Linking of the MAG and genes expressions to the idfiles of COG Pfam, EC and Tigrfam.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#############################FUNCTIONS####################################

# Define count_entries()
def concat_col(df, column1, column2):
    """Return a concatenated MAG and Gene list/dictionary for easy association 
    of gene expression to label? counts of 
    occurrences as value for each key."""
    # Initialize an empty dictionary: langs_count
    col_combo = {}
    # Extract column from DataFrame: col
    col1 = df[column1]
    col2 = df[column2]
    
    col_join = col1 + '|' + col2
    col_combo = dict(col_join)
    return(col_combo)

#Define addMAGGene
def addMAGGene(new_df, dict_of_col):
    """Return a dataframe with the addition of the Column
    with the combined MAG and Gene label"""
    #print(type(dict_of_col))
    add_df = pd.Series(dict_of_col)
    
    new_df.insert(0, 'MAGGene label', add_df)
    #print(new_df.head())
    return(new_df)

#######################FILE INPUT###############################
##Raw counts file
file = '../data/ryno_project/P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv' #input

###############Gene id files################
#COG
idfile1 = '../data/ryno_project/LMO.indiv.MAGs.merged.COG.tsv'

#EC
idfile2 = '../data/ryno_project/LMO.indiv.MAGs.merged.EC.tsv'

#PFAM
idfile3 = '../data/ryno_project/LMO.indiv.MAGs.merged.PFAM.tsv'

#TIGRFAM
idfile4 = '../data/ryno_project/LMO.indiv.MAGs.merged.TIGRFAM.tsv'

list_of_idfile= [idfile1, idfile2, idfile3, idfile4]
list_of_id_names= ['cog','ec','pfam','tigr']
dict_of_idfile= {'cog_df' : idfile1, 'ec_df' : idfile2, 'pfam_df' : idfile3, 'tigr_df' : idfile4}

########################VARIABLES############################
#Raw count column varieble assignment
col_name1 = 'MAG' #input('Please enter the column1 name:')
col_name2 = 'Gene' #input('Please enter the column2 name:')

col_names = ['MAGGene label','Gene ID']


#######################CREATING pandas DATAFRAMES##############################


##Raw counts file
raw_df= pd.read_table(file)
print(raw_df.head())

def create_idfile_df(file_dict):
    count=0
    df_dict= {}
    for key, value in file_dict.items():
        print(value)
        print(key)
        #print(str(i))
        df_dict[key] =  
        #df_dict[key] = pd.read_table(value, header=None, names=col_names)
        count+=1
    #print(df_dict)
    return df_dict

    
    
    #cog_df= pd.read_table(idfile1, header=None)
'''    
#################Head of the whole of idfile1#################
print(str(idfile1))
cog_df= pd.read_table(idfile1, header=None, names=col_names)
#cog_df.columns = col_names
print(cog_df.head())

#################Head of the whole of idfile2#################
print(str(idfile2))
ec_df= pd.read_table(idfile2, header=None, names=col_names)
#ec_df.columns = col_names
print(ec_df.head())

#################Head of the whole of idfile3#################
print(str(idfile3))
pfam_df= pd.read_table(idfile3, header=None, names=col_names)
#pfam_df.columns = col_names
print(pfam_df.head())

#################Head of the whole of idfile4#################
print(str(idfile4))
tigr_df= pd.read_table(idfile4, header=None, names=col_names)
#tigr_df.columns = col_names
print(tigr_df.head())
'''






################################MAIN: FUNCTION CALLING#########################33

# Call concat_col(): result
dict_MAGGene = concat_col(raw_df, col_name1, col_name2)

## Call addMAGGene(): new_df
new_df = addMAGGene(raw_df, dict_MAGGene)
new_df.head()
#Link the MAGGene_label to the idfiles

## Creating pandas dataframe for each idfile in a function
combo_dict= create_idfile_df(dict_of_idfile)
print(combo_dict)

##

#print(combo_dict)
'''
combo_df = pd.DataFrame(combo_dict, index_col= 0)
print(type(combo_df))
print(combo_df.head())
print(combo_df.info())
'''
#combo_df['MAGGene label'] = cog_df['MAGGene label'].unique()
 
#cog_df.iloc[:,0]


#combo_df.insert(0, 'MAGGene label', add_df)

#for lab,row in combo_df.iterrow():
#    print(lab)
#    print(row)

#combo_df= cog_df.iloc[:,0]
#print(combo_df)
#combo_df = pd.DataFrame()
#combo_df.insert(0, 'MAGGene label', add_df)

#print(info)

###Dataframes info############

'''
print(cog_df.info())
print(ec_df.info())
print(pfam_df.info())
print(tigr_df.info())
'''


