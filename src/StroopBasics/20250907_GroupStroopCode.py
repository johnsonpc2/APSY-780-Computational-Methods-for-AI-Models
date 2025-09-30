# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 13:28:35 2025

@author: johns
"""
import numpy as np
import pandas as pd
import seaborn as sns


def generate_rts(n_trials):
    condition = ['congruent', 'incongruent']
    trial_decider = np.random.choice(
        a=condition, size=n_trials, replace=True, p=[.5, .5])

    all_rts = []

    for trial in trial_decider:
        # rt_congruent = False
        if trial == "congruent":
            trial_rt = np.random.normal(400, 100, 1).astype(int)[0]
        else:
            trial_rt = np.random.normal(700, 100, 1).astype(int)[0]

        all_rts.append(trial_rt)

    results = {"trial": np.arange(1, n_trials + 1),
               "condition": trial_decider,
               "rt": all_rts}

    results_df = pd.DataFrame(results)

    return results_df


def analyze_rts(data):
    mean_congruent = data[data['condition'] == 'congruent'].rt.mean()
    mean_incongruent = data[data['condition'] == 'incongruent'].rt.mean()

    print(f"The mean of congruent trials is {round(mean_congruent, 3)}")
    print(f"The mean of incongruent trials is {round(mean_incongruent, 3)}")


results = generate_rts(200)

results.to_csv(
    './OneDrive/Desktop/APSY 780 Computational Methods for AI Models/stroop_data.csv')

analyze_rts(results)

sns.boxplot(results, x="condition", y="rt")
