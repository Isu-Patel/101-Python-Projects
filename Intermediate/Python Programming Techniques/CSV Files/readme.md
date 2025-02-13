# Working with CSV Files in Python

This repository provides a practical guide to working with CSV (Comma Separated Values) files in Python.  It covers reading and writing CSV data using the `csv` module and the `pandas` library, offering clear examples and explanations.

## What are CSV Files?

CSV files are a simple and widely used format for storing tabular data.  Each line in a CSV file represents a row of data, and the values within each row are separated by commas (or other delimiters).

## Reading CSV Files

### Using the `csv` module

The `csv` module is Python's built-in library for working with CSV files.

```python
import csv

# Open the CSV file in read mode ('r')
with open('data.csv', mode='r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)  # Assumes comma as delimiter by default
    # You can specify a different delimiter if needed:  csv.reader(file, delimiter=';')

    # Iterate over each row in the CSV file
    for row in reader:
        # Print each row (which is a list of strings)
        print(row)

# Example with header row:
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file) # Reads each row as a dictionary using the first row as keys.
    for row in reader:
        print(row)
        print(row['column1']) # Accessing data by column name.
