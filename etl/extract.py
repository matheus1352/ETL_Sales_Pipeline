import pandas as pd
from config import CSV_FILE_PATH, JSON_FILE_PATH

def extract_data():
    csv_data = pd.read_csv(CSV_FILE_PATH)
    json_data = pd.read_json(JSON_FILE_PATH)
    data = pd.concat([csv_data, json_data], ignore_index=True)
    return data
