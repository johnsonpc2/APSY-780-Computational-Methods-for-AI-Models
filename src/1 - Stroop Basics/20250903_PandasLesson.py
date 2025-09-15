# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 14:09:33 2025

@author: johns
"""
import pandas as pd

df = pd.read_csv(
    'C:/Users/johns/OneDrive/Desktop/APSY 780 Computational Methods for AI Models/rts_exp.csv')

mean_congruent = df[df['condition'] == 'congruent'].rt.mean()

print(df.head())
print(mean_congruent)
