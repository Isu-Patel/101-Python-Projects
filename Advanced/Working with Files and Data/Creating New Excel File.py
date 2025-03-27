import openpyxl

def create_excel_file(file_path, data):
    workbook = openpyxl.Workbook()
    workbook.save(file_path)

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    for row in data:
        worksheet.append(row)
    workbook.save(file_path)

new_excel_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\new_file.xlsx"
create_excel_file(new_excel_path, [['Name', 'Id'], ['Alice', 1], ['Bob', 2], ['Charlie', 3]])
# This code creates a new Excel file and writes data to it using openpyxl.
