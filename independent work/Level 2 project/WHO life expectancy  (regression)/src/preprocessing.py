import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    return data

def clean_col_names(data):
    data.columns = data.columns.str.strip()
    return data

def drop_missing_target(data):
    data.dropna(subset=['Life expectancy'], axis=0, inplace=True)
    return data

def drop_selected_features(data):
    data.drop(columns=['Population','Hepatitis B','Diphtheria'], inplace=True) 
    return data

def preprocess_data(data):
    cleaned_data = clean_col_names(data)
    cleaned_data = drop_missing_target(cleaned_data)
    cleaned_data = drop_selected_features(cleaned_data)
    return cleaned_data 

def split_features_target(data):
    x = data.drop(columns=["Life expectancy"])
    y = data["Life expectancy"]

    return x, y