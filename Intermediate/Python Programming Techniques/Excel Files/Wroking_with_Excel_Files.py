import pandas as pd

# Define a dictionary with sample data
data = {
    'Name': ['Isu', 'Hetvi', 'Atul'],
    'Age': [13, 13, 13],
    'City': ['Gujrat', 'Gujrat', 'Gujrat'],
    'Phone': [9978717871, 9978717871, 9978717871]  # Add missing phone numbers
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

# Read the Excel file into a DataFrame
df_excel = pd.read_excel('output.xlsx')

# Print the DataFrame read from the Excel file
print(df_excel)

# ------------------------ Output ------------------------------- #
# Name  Age   City Phone
# 0  Isu  13  Gujrat  9978717871
# 1  Hetvi  13  Gujrat  9978717871
# 2  Atul  13  Gujrat  9978717871
