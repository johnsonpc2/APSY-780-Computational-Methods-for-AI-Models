# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 13:14:19 2025

@author: johns
"""


# When you specify a default value for an argument, every other argument
# followig that argument should also have a defualt specified

def classify_rts(list_rts, threshold=500):

    for rt in list_rts:
        is_rt_long = False
        # str_long_short = "Short"
        if rt > threshold:
            is_rt_long = True
            # str_long_short = "Long"

        str_long_short = 'Long' if is_rt_long else 'Short'
        print(f"Here is an RT: {rt}. This RT is {str_long_short}")


rts = [450, 700, 650, 375, 550, 475, 595]

classify_rts(rts)
