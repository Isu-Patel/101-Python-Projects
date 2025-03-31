import csv

def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

csv_file_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\sample.csv"
new_data = [['Age'], [14], [39], [40]]

