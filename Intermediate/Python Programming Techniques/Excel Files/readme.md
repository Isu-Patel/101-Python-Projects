# Working with Excel Files in Python

This repository demonstrates how to read and write data to Excel files using the `pandas` library in Python.  Excel is a widely used spreadsheet format, and `pandas` provides a powerful and convenient way to interact with it.

## What are Excel Files?

Excel files are used to store data in a structured tabular format, organized into rows and columns.  They can contain multiple worksheets, each acting as a separate table.

## Reading Excel Files

The `pandas` library makes reading Excel files straightforward:

```python
import pandas as pd  # It's common to import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('output.xlsx')  # Reads the first sheet by default. You can specify sheet_name='Sheet2' etc.

# Print the DataFrame
print(df)

# Accessing data:
print(df['Name'])      # Access a column (Series)
print(df.loc)        # Access a row by label or index
print(df.iloc)     # Access a specific element by integer position
print(df.head())       # Prints the first 5 rows
print(df.describe())  # Get descriptive statistics of numerical columns

# Reading from a specific sheet:
df_sheet2 = pd.read_excel("output.xlsx", sheet_name="Sheet2") # Or sheet_name=1 for the second sheet.

# Specifying data types:
df_mixed_types = pd.read_excel("output.xlsx", dtype={"Age": str, "Phone": int}) #Force data types.

# Handling missing data:
df_missing = pd.read_excel("output.xlsx", na_values=["N/A", "NaN", ""]) #Treat these as missing values.
print(df_missing.fillna(0)) # Fill missing values with 0.
