# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:30:37 2017

@author: Bioviking
"""
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

###Example file1 = '../P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv'

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
        

# Define count_entries()
'''
def count_entries(new_df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
  
    print(new_df.head())
    print(col_name)
    print(new_df[col_name].describe())
    
    
    df_col_count = df_col_unique.count()
    print('This is df_col_count', df_col_count)
    return(df_col_count)
 
    # Initialize an empty dictionary: col_count
    col_count = {}
    print(new_df[col_name].describe())
    col_unique = new_df[col_name].unique()
    df_col_unique = pd.Series(col_unique)
    print(df_col_unique)
    for ele in df_col_unique:
        indices = new_df[col_name] == str(ele)
        col_count[ele] = new_df.loc[indices,:]
        
        
    #print(indices = True)
        #setosa = iris.loc[indices,:]
        #print(ele)
        #bins_count = new_df[new_df[col_name] == str(ele)].count()
        #col_count[ele] = bins_count 
    print('This is col', col_count)
    
    for ele in new_df[col_name]:
        #print(ele)
        col_count[ele] = new_df[new_df[col_name] == ele].count()
    print('This is col', col_count)
    return
   
        try:
            
            # Extract column from DataFrame: col
            col = new_df[ele]
            print(col)
            
            # Iterate over MAG column in DataFrame
            for entry in col:
        
                # If the MAG is in MAG_count, add 1
                if entry in col_count.keys():
                    col_count[entry] += 1
                # Else add the MAG to MAG_count, set the value to 1
                else:
                    col_count[entry] = 1
            df_col_count = pd.DataFrame(col_count)
            # Return the col_count Dataframe
            
            return(df_col_count)
            
        except:
            
            print('The DataFrame does not have a ' + ele + ' column.')
            #print('Please ensure it is one of the following column' )
'''


#Define addMAGGene
def addMAGGene(new_df, dict_of_col):
    """Return a datafram with the addition of the Column
    with the combined MAG and Gene label"""
    #print(type(dict_of_col))
    add_df = pd.Series(dict_of_col)
    
    new_df.insert(0, 'MAGGene_label', add_df)
    #print(new_df.head())
    return(new_df)

#def GeneXvsT():
  #  """Return a numpy array of all Genes and their gene exp in each sample"""
 #   return(np_gene_x)

#Define create_array
def create_array(info_in):
    """Return a a numpy array created out of a list or dictionary"""
    print(type(info_in))
    try:
        np_x = np.array(info_in[:,1])
        
        #list_dict_values= [i for i in info_in.values()]
         #   np_x = np.array(list_dict_values)
    
        return(np_x)
    except:
        print('Please ensure its a list or dictionary')
        
#######################USER INPUT###############################
file = '../P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv' #input('Please enter the file name:')
#INPUT OPTIONS
#col_name = str(input('Please enter the column name:'))
col_name = 'MAG'

col_name1 = 'MAG' #input('Please enter the column1 name:')
col_name2 = 'Gene' #input('Please enter the column2 name:')
#list_gene_values = []

print(file)
print(col_name)
print(col_name1)
print(col_name2)

#print(str(file))
df= pd.read_table(file)
#print(df.head())

################################MAIN: FUNCTION CALLING#########################33
# Call concat_col(): result
dict_MAGGene = concat_col(df, col_name1, col_name2)

## Call addMAGGene(): new_df
new_df = addMAGGene(df, dict_MAGGene)

#############################################ROUGH#############
'''
Counting the number of Genes expressed per a Organisms(MAG)
Done by count the number of time a MAG label appears in the column MAG

'''
#Uniques MAG labels
MAG = list(new_df[col_name].unique())
#print(MAG)

#The Whole MAG list from file
MAG_col = list(new_df[col_name])
#print(MAG_col)

list_count = [MAG_col.count(i) for i in MAG]
#print(list_count)

#Create dictionary
MAG_count= { 'MAG': MAG, 'Counts': list_count}

list_labels = ['MAG','Counts'] 
list_col= [MAG, list_count]

zipped= list(zip(list_labels, list_col))
print(zipped)

MAG_count = dict(zipped)


#Create a DataFrame of MAG and no of Gene per a MAG in 2 columns
MAG_df = pd.DataFrame(MAG_count, columns = ['MAG', 'Counts'])
print(MAG_df)

y ='Counts'
MAG_df.hist(y, bins=83)
plt.xlabel('Genes per a MAG')
plt.title('Histogram of Gene')
plt.show()

##################################################################3

#No of genes per a MAG
# Call count_entries() for : df_count_result
#df_count_result = count_entries(new_df, col_name)

#Gene_result = count_entries(new_df, col_name2)
#Gene
#Creating a numpy array for plotting
#list_gene_values= [i for i in count_result.values()]
#np_x = np.array(list_gene_values)


# Call GeneXvsT() for : np_gene_x
#np_gene_exp = GeneXvsT(new_df, col_name2)


#np_x = create_array(df_count_result)

#######################Setup of plots#############################

# Definition of tick_val and tick_lab
#tick_val = [1000,10000,100000]
#tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
#plt.xticks(tick_val, tick_lab)
#no_bins = 83
#plt.xlabel('# of Genes per a MAG')
#plt.ylabel('# of MAGs with a number of genes in range')
#plt.title('Distribution of MAGs with number of genes')

#######################Setup of plots#############################
'''
# Definition of tick_val and tick_lab
tick_val = [20,40,60,80]
tick_lab = ['20','40','60','80']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)
#no_bins = 83
plt.xlabel('Genes found in MAG')
plt.ylabel('# of each Gene present in across all MAGs')
plt.title('Genes transcript count')


#Print the output as Plot to Screen
plt.plot(np_x)
#plt.hist()
plt.show()
plt.clf()
'''


#############################Plotting Histograms####################

#plt.hist(x, bins= 6)
#plt.hist2d(x, y, bins= (len(list_uniqmag)+1), histtype= 'bar')
#plt.show()
#plt.clf()

####################Plotting Scatter plot##################3

#plt.hist2d(x2,)




#################################OUTPUT#####################################
###############################Text2Screen###################################

#print(dict_MAGGene)
#print(new_df.head())
#print(df_count_result)
#print(Gene_result)

#print(list_gene_values)

#plt.show()
#plt.clf()


###########################Print to file#######################


