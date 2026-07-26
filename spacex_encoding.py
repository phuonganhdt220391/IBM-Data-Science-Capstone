# spacex_encoding.py
import pandas as pd

print("Applying One-Hot Encoding to categorical features...")

# Example columns typically encoded in the capstone: Orbit, LaunchSite, LandingPad, Series
def apply_one_hot_encoding(df):
    categorical_cols = ['Orbit', 'LaunchSite', 'LandingPad', 'Series']
    existing_cols = [col for col in categorical_cols if col in df.columns]
    
    if existing_cols:
        df_encoded = pd.get_dummies(df, columns=existing_cols)
        print(f"Encoded columns: {existing_cols}")
        return df_encoded
    return df

print("One-hot encoding module ready.")