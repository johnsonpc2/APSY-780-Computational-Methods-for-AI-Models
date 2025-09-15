# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:18:03 2025

@author: johns
"""
import numpy as np


class Coin:
    """
    A simple class for a coin. Has value of coin and sides.
    You can flip the coin
    """

    sides = ['heads', 'tails']  # class attributes, shared by all instances

    def __init__(self, value=25):  # constructor
        self.value = value  # an instance attribute specific to this instance
        self.side_up = self.sides[0]
        self.rng = np.random.default_rng(seed=50)

    def __repr__(self):
        return f"I'm a Coin. My value is {self.value} and I'm facing {self.side_up} side up."

    def flip(self):
        self.side_up = self.rng.choice(self.sides)


pocket_coin1 = Coin(value=10)
pocket_coin2 = Coin()

print(pocket_coin1)
print(pocket_coin2)
