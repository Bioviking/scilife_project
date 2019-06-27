# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:32:02 2017

@author: Bioviking
"""
import numpy as np
import pandas as pd

file = '/./data/ryno_project/P3764_P1456.LMO.indiv.MAGs.merged.raw_counts.tsv'

df= pd.read_table(file)
print(df.head())