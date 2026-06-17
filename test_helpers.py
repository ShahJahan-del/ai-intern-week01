# test_helpers.py
import pandas as pd
import pytest
from helpers import (
    fill_missing_ages,
    fill_missing_embarked_data,
    fill_missing_deck,
    encode_gender
)

def test_fill_missing_ages():
    data = {'age': [20, None, 40, 30]}
    df = pd.DataFrame(data)
    df_cleaned = fill_missing_ages(df)
    assert df_cleaned['age'].isnull().sum() == 0
    assert df_cleaned['age'].iloc[1] == 30.0

def test_fill_missing_embarked_data():
    # 'S' appears twice for embarked, 'Cherbourg' appears twice for embark_town
    data = {
        'embarked': ['S', 'C', 'S', None],
        'embark_town': ['Cherbourg', 'Southampton', 'Cherbourg', None]
    }
    df = pd.DataFrame(data)
    df_cleaned = fill_missing_embarked_data(df)

    # Vérifications pour embarked
    assert df_cleaned['embarked'].isnull().sum() == 0
    assert df_cleaned['embarked'].iloc[3] == 'S'

    # Vérifications pour embark_town
    assert df_cleaned['embark_town'].isnull().sum() == 0
    assert df_cleaned['embark_town'].iloc[3] == 'Cherbourg'

def test_fill_missing_deck():
    # NAs mus be replaced by 'Unknown'
    data = {'deck': ['A', None, 'C']}
    df = pd.DataFrame(data)
    df_cleaned = fill_missing_deck(df)
    assert df_cleaned['deck'].isnull().sum() == 0
    assert df_cleaned['deck'].iloc[1] == 'Unknown'

def test_encode_gender():
    data = {'sex': ['male', 'female', 'male']}
    df = pd.DataFrame(data)
    df_encoded = encode_gender(df)
    assert list(df_encoded['sex_encoded']) == [1, 0, 1]



