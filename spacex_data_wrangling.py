# spacex_data_wrangling.py
import pandas as pd
import numpy as np

print("Starting Data Wrangling & Cleaning...")

# Simulated data frame cleaning steps from IBM capstone
# 1. Handling missing values with mean imputation for payload mass
# 2. Converting landing outcomes into binary classification targets (1 = Success, 0 = Failure)

def wrangle_data(df):
    if 'PayloadMass' in df.columns:
        mean_payload = df['PayloadMass'].mean()
        df['PayloadMass'].fillna(mean_payload, inplace=True)
    
    if 'LandingOutcome' in df.columns:
        success_outcomes = ['True RTLS', 'True ASDS', 'True Ocean']
        df['Class'] = df['LandingOutcome'].apply(lambda x: 1 if x in success_outcomes else 0)
        
    return df

print("Data wrangling script template initialized successfully.")