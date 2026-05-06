import pandas as pd

def get_excel_data(file_path):
    df=pd.read_excel(file_path)
    return df.values.tolist()