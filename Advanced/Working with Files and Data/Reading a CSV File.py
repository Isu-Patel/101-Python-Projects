import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    return data

csv_file_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\sample.csv"
csv_data = read_csv_file(csv_file_path)
print(csv_data)
# This code reads a CSV file and prints its content using the csv module.
