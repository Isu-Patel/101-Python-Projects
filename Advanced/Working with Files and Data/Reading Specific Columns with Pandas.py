import pandas as pd

def read_specific_columns(file_path, columns):
    # Read the Excel file using pandas, specifying the columns to read
    df = pd.read_excel(file_path, usecols=columns)
    return df

excel_file_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\test.xlsx"
selected_columns = ['Name', 'Id']  # Specify the columns you want to read
selected_data = read_specific_columns(excel_file_path, selected_columns)
print(selected_data)
