# helpers.py
import pandas as pd

def fill_missing_ages(df):
    """Remplace les valeurs manquantes de la colonne 'age' par la médiane."""
    median_age = df['age'].median()
    df['age'] = df['age'].fillna(median_age)
    return df

def encode_gender(df):
    """Encode la colonne 'sex' en valeurs numériques (1 pour male, 0 pour female)."""
    df['sex_encoded'] = df['sex'].map({'male': 1, 'female': 0})
    return df