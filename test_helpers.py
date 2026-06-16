# test_helpers.py
import pandas as pd
import pytest
from helpers import fill_missing_ages, encode_gender

def test_fill_missing_ages():
    # 1. On crée un faux DataFrame de test avec des valeurs manquantes (None)
    data = {'age': [20, None, 40, 30]}
    df = pd.DataFrame(data)

    # 2. On applique ta fonction (la médiane de 20, 40, 30 est 30)
    df_cleaned = fill_missing_ages(df)

    # 3. On vérifie (assert) qu'il n'y a plus de valeurs manquantes
    assert df_cleaned['age'].isnull().sum() == 0
    # On vérifie que le "None" a bien été remplacé par la médiane (30.0)
    assert df_cleaned['age'].iloc[1] == 30.0

def test_encode_gender():
    # 1. On crée un faux DataFrame avec des genres en texte
    data = {'sex': ['male', 'female', 'male']}
    df = pd.DataFrame(data)

    # 2. On applique la fonction d'encodage
    df_encoded = encode_gender(df)

    # 3. On vérifie que la nouvelle colonne contient les bonnes valeurs
    assert list(df_encoded['sex_encoded']) == [1, 0, 1]