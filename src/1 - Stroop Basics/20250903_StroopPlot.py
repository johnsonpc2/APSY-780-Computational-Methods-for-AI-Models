# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 13:15:54 2025

@author: johns
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    'C:/Users/johns/OneDrive/Desktop/APSY 780 Computational Methods for AI Models/rts_exp.csv')
print(df.head())

# Draw a lineplot of RTs
# sns.lineplot(df, x='trial', y='rt')
sns.boxplot(df, x='condition', y='rt')
plt.title('RT comparisons across conditions')
plt.xlabel('Conditions')
plt.ylabel('RTs (ms)')
plt.show()
