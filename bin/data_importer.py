# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:32:02 2017

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

#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
print(df.info())
print('\n')
print('\n')
print('\n')

#################Head of the whole of file2#################
print(str(file2))
df= pd.read_table(file2)
print(df.head())

#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
print(df.info())
print('\n')
print('\n')
print('\n')

#################Head of the whole of file3#################
print(str(file3))
df= pd.read_table(file3)
print(df.head())

#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
print(df.info())
print('\n')
print('\n')
print('\n')

#################ExcelFile Head of the whole of file4#################
print(str(file4))
xl= pd.ExcelFile(file4)

print(xl.sheet_names)

###Print Column no.1#####
#### eg. df2 = xl.parse(1, parse_cols=[0], skiprows= [0], names=['Country'])
xl1 = xl.parse(0, parse_cols=[0]) #'Sheet1' xl1 = xl.parse('Sheet1')
print(xl1) 


#print(df.head())
#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
#print(df.info())

#print(xl1)


#################Head of the whole of idfile1#################
print('\n')
print('\n')
print('\n')
df= pd.read_table(idfile1)
print(df)
#print(df.head())

#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
print(df.info())


#################Head of the whole of idfile2#################
print('\n')
print('\n')
print('\n')
print(str(idfile2))
df= pd.read_table(idfile2)
print(df.head())

#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
print(df.info())
print('\n')
print('\n')
print('\n')

#################Head of the whole of idfile3#################
print(str(idfile3))
df= pd.read_table(idfile3)
print(df.head())

#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
print(df.info())
print('\n')
print('\n')
print('\n')

#################Head of the whole of idfile4#################
print(str(idfile4))
df= pd.read_table(idfile4)
print(df.head())

#print(df.index)
#print(df.columns)
#print(df.shape)
#print(type(df))
#print(type(df.index))
#print(df.iloc[:5,:])   #First 5
#print(df.iloc[-5:,:])  #Last 5
print(df.info())
print('\n')
print('\n')
print('\n')


####Code for a histogram###



'''

# Set number of time points to sample: num_samples
num_samples= 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show() 




pd.DataFrame.hist(df[1:[2:]])
plt.xlabel('Sample')
plt.ylabel('Number of Genes')
plt.show()

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()



# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()
'''