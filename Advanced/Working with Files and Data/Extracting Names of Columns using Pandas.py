import pandas as pd
from pyparsing import col

def extract_column_names(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Extract column names
    column_names = df.columns.tolist()
    
    return column_names

excel_file_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\test.xlsx"
column_names = extract_column_names(excel_file_path)
print("Column names in the Excel file:", column_names)
