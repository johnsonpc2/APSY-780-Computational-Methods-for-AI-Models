# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 14:01:45 2025

@author: johns
"""

rts = [550, 620, 430, 390, 480, 550, 620, 430, 390, 480]
sum_rts = sum(rts)
avg_rts = sum_rts / len(rts)

print(f"Here is my lits of RTs: {rts}")
print(f"Number of RTs in the list: {len(rts)}")
print(f"The average RT is: {avg_rts}")
print(f"First RT: {rts[0]}")
print(f"Last RT: {rts[-1]}")
print(f"Firt 5 RTs: {rts[:5]}")
print(f"Last 3 RTs: {rts[-3:]}")
