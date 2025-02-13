import csv

# Open the CSV file in read mode
with open('data.csv', mode='r') as file:
    # Create a CSV reader object using the file object
    reader = csv.reader(file)
    # Iterate over each row in the CSV file
    for row in reader:
        # Print each row of the CSV file
        print(row)

# Read the CSV file into a DataFrame
# The pandas library provides a convenient way to read a CSV file into a DataFrame,
# which is a tabular data structure that can be easily manipulated and analyzed.
import pandas

df = pandas.read_csv('data.csv')

# Print the DataFrame
# The DataFrame is a tabular data structure that can be easily printed to the console
# The to_string() method is used to convert the DataFrame to a string
print(df.to_string())
