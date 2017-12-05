# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:55:36 2017

Script to run DESeq2 with R through python

@author: Admin
"""

from numpy import zeros
from numpy.random import multinomial, random
from rpy2 import robjects
#import rpy2.robjects.numpy2ri
#robjects.numpy2ri.activate()

from rpy2.robjects import Formula
from rpy2.robjects.packages import importr
deseq = importr('DESeq2')

# Generate some data. 1000 genes, 10 samples
n = 1000
probabilities = random(n)
probabilities /= sum(probabilities)
data = zeros((n,10), int)
for i in range(10):
    data[:,i] = multinomial(1000000, probabilities)

# Make the data frame
d = {}
categories = ('1','2') * 5
d["key_1"] = robjects.IntVector(categories)
dataframe = robjects.DataFrame(d)

# Create the design matrix, and run DESeqDataSetFromMatrix
design = Formula("~ key_1") # <--- I guess this is wrong
dds = deseq.DESeqDataSetFromMatrix(countData=data, colData=dataframe,design=design)


