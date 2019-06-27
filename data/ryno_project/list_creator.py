import sys


f = open('P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv', 'r+')  #./data/ryno_project/
alllines = f.readlines()
#alllines = alllines.strip()
firstline = alllines[0]
firstline = firstline.split()
print(firstline)

#############First line list creation################
sample_list= []
col_list = [] 
for i in firstline:    
    print(i)
    col_list.append(i)
    if len(i) == 6:
        sample_list.append(i)
print(col_list)
print(sample_list)


#########################MAGs and Gene List creations####################
mags_list = []
gene_list = []
mag_dict = {}
for row in alllines[1:]:
    temp_row = row
    temp_row = temp_row.split()
    mag_dict[temp_row[0]] = temp_row[0] 
    #if temp_row not in mags_list:
    #    mags_list.append(temp_row[0])
        
    #gene_list.append(temp_row[1])
    #print(temp_row)
    
print(mag_dict.keys)    
print(len(mags_list), len(gene_list))
