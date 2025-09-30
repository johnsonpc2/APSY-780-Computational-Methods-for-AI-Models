# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 14:25:56 2025

@author: johns
"""


def mean_rt(rt_list):
    rt_sum = sum(rt_list)
    n_rt = len(rt_list)
    rt_mean = rt_sum / n_rt
    return rt_mean


rts = [550, 620, 430, 390, 480, 550, 620, 430, 390, 480]

print(f"Mean RT: {mean_rt(rts)}")
