# helpers.py
import pandas as pd

def fill_missing_ages(df):
    """Replace the age column NAs by the median."""
    median_age = df['age'].median()
    df['age'] = df['age'].fillna(median_age)
    return df

def fill_missing_embarked_data(df):
    """Replace the 'embarked' and 'embark_town' columns NAs by their respective modes."""
    if 'embarked' in df.columns and not df['embarked'].dropna().empty:
        df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

    if 'embark_town' in df.columns and not df['embark_town'].dropna().empty:
        df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
    return df

def fill_missing_deck(df):
    """Replace the deck column NAs by the 'Unknown' category."""
    df['deck'] = df['deck'].fillna('Unknown')
    return df

def encode_gender(df):
    """Encode the sex column into numerical values (1 male, 0 for female)."""
    df['sex_encoded'] = df['sex'].map({'male': 1, 'female': 0})
    return df