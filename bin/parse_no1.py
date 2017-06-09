#Parsing of this file
#./data/ryno_project/P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv
../data/ryno_project/P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv


f = open('../data/ryno_project/P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv', 'r+')
print(f)

for line in f:
	print(line[0])
