import pandas as pd

def read_excel_with_pandas(file_path):
    # Read the Excel file using pandas
    df = pd.read_excel(file_path)
    
    return df

excel_file_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\test.xlsx"
data_frame = read_excel_with_pandas(excel_file_path)
print(data_frame)
