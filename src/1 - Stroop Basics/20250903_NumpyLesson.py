# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 13:44:24 2025

@author: johns
"""
import numpy as np


def random_rts(num_rts=10, mean=500, std=100):
    rt_array = np.random.normal(num_rts, mean, std).astype(int)

    return rt_array


rts_array = random_rts()


# Use numpy to calculate the mean, median, and the standard deviation of
# the RTs

# rts = [450, 550, 650, 750]
# rts_array = np.array(rts)

print(f"Mean RT: {np.mean(rts_array)}")
print(f"Median RT: {np.median(rts_array)}")
print(f"SD of RT: {np.std(rts_array)}")
