# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 13:28:35 2025

@author: johns
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

wd = os.getcwd()


#  Define a function to generate RT data from a stroop task
def generate_rts(n_trials, n_subs, remove_practice):
    """
    Generate RT data from a stroop task for multiple subjects.

    Parameters:
    -----------
    n_trials : int
        The number of trials per subject
    n_subs : int
        The number of subjects to generate data for

    Returns:
    --------
    results_df : pd.DataFrame
        Combined data from all subjects
    """

    # Create empty lists for each variable to store all data across subjects
    all_trials = []
    all_conditions = []
    all_rts = []
    all_subjects = []

    # Outer loop: iterate through each subject
    for subject in range(1, n_subs + 1):

        # Sample random parameters for this subject's distributions, starting
        # with the congruent sampling distributions
        congruent_mean = np.random.normal(400, 50, 1)[0]  # Mean RT
        congruent_std = abs(np.random.normal(50, 10, 1)[
                            0])  # RT SD (must be positive)

        # And now do the same for the incongruent distributions
        incongruent_mean = np.random.normal(700, 50, 1)[0]  # Mean RT
        incongruent_std = abs(np.random.normal(50, 10, 1)[0])  # RT  SD

        # Randomly decide if a trial is congruent or incongruent
        condition = ['congruent', 'incongruent']
        trial_decider = np.random.choice(
            a=condition, size=n_trials, replace=True, p=[.5, .5])

        # Inner loop: iterate through each trial for this subject
        for trial_idx, trial_condition in enumerate(trial_decider):

            # Generate RT based on the trial condition using parameters above
            if trial_condition == "congruent":
                trial_rt = np.random.normal(
                    congruent_mean, congruent_std, 1).astype(int)[0]
            else:
                trial_rt = np.random.normal(
                    incongruent_mean, incongruent_std, 1).astype(int)[0]

            # Append data to the lists
            all_trials.append(trial_idx + 1)  # Trial number (1 to n_trials)
            all_conditions.append(trial_condition)
            all_rts.append(trial_rt)
            all_subjects.append(subject)

    # Create the results dataframe
    results = {
        "subject": all_subjects,
        "trial": all_trials,
        "condition": all_conditions,
        "rt": all_rts
    }
    results_df = pd.DataFrame(results)

    # Remove N practice trials from the beginning of each subject's data
    if remove_practice > 0:
        # Create an empty list to store filtered data
        filtered_data = []

        # For each subject, remove the first 'remove_practice' trials
        for subject in results_df['subject'].unique():
            subject_data = results_df[results_df['subject'] == subject]
            # Keep only trials after the practice trials
            subject_filtered = subject_data.iloc[remove_practice:]
            filtered_data.append(subject_filtered)

        # Combine all filtered subject data
        results_df = pd.concat(filtered_data, ignore_index=True)

    return results_df


def analyze_rts(data):
    #  Analyze RT data across all subjects
    print("=== OVERALL ANALYSIS ===")
    mean_congruent = data[data['condition'] == 'congruent'].rt.mean()
    mean_incongruent = data[data['condition'] == 'incongruent'].rt.mean()
    var_congruent = data[data['condition'] == 'congruent'].rt.std()
    var_incongruent = data[data['condition'] == 'incongruent'].rt.std()

    print(f"The mean of congruent trials is {round(mean_congruent, 3)}")
    print(
        f"The standard deviation of congruent trials is {round(var_congruent, 3)}")
    print(f"The mean of incongruent trials is {round(mean_incongruent, 3)}")
    print(
        f"The standard deviation of incongruent trials is {round(var_incongruent, 3)}")

    print("=== BY-SUBJECT ANALYSIS ===")
    # Loop through each subject to show individual statistics
    for subject in data['subject'].unique():
        subject_data = data[data['subject'] == subject]

        subj_congruent = subject_data[subject_data['condition']
                                      == 'congruent'].rt.mean()
        subj_incongruent = subject_data[subject_data['condition']
                                        == 'incongruent'].rt.mean()
        stroop_effect = subj_incongruent - subj_congruent

        print(f"Subject {subject}: Congruent RT avg: {round(subj_congruent, 2)}",
              f"Incongruent RT avg: {round(subj_incongruent, 2)}",
              f"Stroop Effect: {round(stroop_effect, 2)} ms")


results = generate_rts(n_trials=500, n_subs=6, remove_practice=20)

results.to_csv(
    '~/OneDrive/Desktop/APSY 780 Computational Methods for AI/stroop_data.csv',
    index=False
)

data = pd.read_csv(
    '~/OneDrive/Desktop/APSY 780 Computational Methods for AI/stroop_data.csv'
)

analyze_rts(data)

plt.figure(figsize=(8, 6))
sns.boxplot(data, x="condition", y="rt")
plt.title("Group-Level Stroop RTs")
plt.ylabel("Reaction Time (ms)")
plt.xlabel("Condition")
plt.savefig('C:/Users/johns/OneDrive/Desktop/APSY 780 Computational Methods for AI/20250913_GroupStroopPlot.png',
            dpi=600, bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x="condition", y="rt", hue="subject", palette="Dark2")
plt.title("RT by Condition for All Subjects")
plt.ylabel("Reaction Time (ms)")
plt.xlabel("Condition")
plt.legend(title="Subject", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('C:/Users/johns/OneDrive/Desktop/APSY 780 Computational Methods for AI/20250913_IndividualStroopPlot.png',
            dpi=600, bbox_inches='tight')
plt.show()
