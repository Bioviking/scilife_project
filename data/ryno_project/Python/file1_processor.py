# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:28:21 2017

@author: Bioviking
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file1 = '../P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv'

#################Head of the whole of file1#################
print(str(file1))
raw_df= pd.read_table(file1)
#print(raw_df.head())

#################Data info Code##################### 
#print(raw_df.index)
#print(raw_df.columns)
#print(raw_df.shape)
#print(type(raw_df))
#print(type(raw_df.index))
#print(raw_df.iloc[:5,:])   #First 5
#print(raw_df.iloc[-5:,:])  #Last 5
#print(raw_df.info())
#print('\n')
#print('\n')
#print('\n')

######################Function#################
######################Reading Column##########################

out_df= raw_df.groupby('MAG')['Gene'].count()
print(out_df)

out_df.to_csv('../output_MAGGene_counts.csv')

out2_df = raw_df.groupby('Gene')['MAG'].count()

print(out2_df)

out2_df.to_csv('../output2_MAGGene_counts.csv')

'''
###########Creating a MAG and Genes list#################

list_mag = list(df.iloc[:,0])
print(len(list_mag))
#print(list_mag[:50])
list_geneid = list(df.iloc[:,1])
list_uniq_geneid = list(set(list_geneid))
print('this is length of gene id list', len(list_geneid))
print('this is length of uniq gene id list', len(list_uniq_geneid))

#print(list_geneid[:50])
#print(df.iloc[:,2:])
sample = df.iloc[:,2:]
list_sample = list(df.iloc[:,2:])
print(list_sample)
print('this is length of sample list', len(list_sample))

list_samplelist= [df.iloc[:,i] for i in range(0 , len(list_sample))]
#print(list_samplelist[2])
#print(len(list_samplelist))

############Creating the uniques MAG list#############3

list_uniqmag = list(set(list_mag))
#print(len(list_uniqmag))
#print(list_uniqmag)
#print('\n')

list_uniqmag.sort()
#print('\n')

###################Count number of genes per MAG###############33

temp_list = []
dict_gene_count = {}
list_gene_count = []
list_mag_index = []
for i in list_uniqmag:    
    #temp_list.append(i) 
    if i in list_mag:  
        dict_gene_count[i] = list_mag.count(i)
        list_gene_count.append(list_mag.count(i))
        list_mag_index.append(list_uniqmag.index(i))
    gene_count = 0
#print(list_mag_index)    
print('This is dict of gene count', len(dict_gene_count))

##############################No of genes in each sample###############
dict_gene_exp= {}
dict_mag_gene= {}
for i in list_sample:
    #print(df.loc[:50,['MAG', 'Gene',i]])
    MAG_gene_sample = df.loc[:,['MAG', 'Gene',i]]
    #print(MAG_gene_sample)
    
    temp_value = [value for value in df.loc[:,[i]] ]
    #print(temp_value)
    dict_mag= dict(df[['MAG']])
    dict_gene = [gene for gene in df[['Gene']]]
    dict_mag_gene[dict_mag]= dict_gene
    print('This is a dict of ', dict_mag_gene)
    #temp_key = [key for key in df[['MAG','Gene']]]
    
    #print(temp_key)
    #if temp_value > 0 :
     #   dict_gene_exp[temp_key] = temp_value
    #else:
     #   next
#print(dict_gene_exp)


########################Array info##########################
x = np.array(list_gene_count)
print(x.shape)
#y = np.array(list_mag_index)
#print(x)
#print(y.shape)

x2 = np.array(list_samplelist[2:])
print(x2.shape)
y2 = np.array(list_sample[2:])


#print('This is the mean', np.mean(x))
#print('This is the median', np.median(x))

#######################Setup of plots#############################
# Definition of tick_val and tick_lab
#tick_val = [1000,10000,100000]
#tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
#plt.xticks(tick_val, tick_lab)
#no_bins = 83
plt.xlabel('# of Genes per a MAG')
plt.ylabel('# of MAGs with a number of genes in range')
plt.title('Distribution of MAGs with number of genes')


#############################Plotting Histograms####################
plt.hist(x, bins= 6)
#plt.hist2d(x, y, bins= (len(list_uniqmag)+1), histtype= 'bar')
#plt.show()
plt.clf()
####################Plotting Scatter plot##################3

#plt.hist2d(x2,)

#plt.show()
plt.clf()



####################
#for key, value in dict_gene_count.items():



#set_mags =
#print(len(set_mags))



#print(list_uniqmag)
#print('\n')
#print(sorted(list_uniqmag))
 
#print('\n')   
#print(list_mag[ele], list_geneid[ele])

#list_mag_genes = [list_geneid[ele] for ele in range(len(list_mag)) for uniq_mag in list_uniqmag  if list_mag[ele] == uniq_mag]
#print(list_mag_genes)

#for m, g in zip(list_mag, list_geneid):
#    print(m,g)
dict_mag_genes = {}
for uniq_mag in list_uniqmag:
    temp_list = []
    #print(uniq_mag)
    for ele in range(len(list_mag)):
        if uniq_mag == list_mag[ele]:            
            temp_list.append(list_geneid[ele])
    dict_mag_genes[uniq_mag] = sorted(temp_list)
#print(dict_mag_genes)

#for counter, key in enumerate(dict_mag_genes.keys()):        
#    gene_count = len(dict_mag_genes[key])
    #print(counter, gene_count)

#for  in range(len(dict_mag_genes)):    
#    print(dict_mag_genes[i])
    
    
    
    

    print(ele)
    temp_listele = ele
    if ele == 
'''