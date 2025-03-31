import openpyxl

def append_values(file_path, sheet_name, values):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.create_sheet(sheet_name)

    for row in values:
        sheet.append(row)

    workbook.save(file_path)

execl_file_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\new_file.xlsx"
new_values = [['Name', 'ID'], ['Isu', 1], ['Atul', 2], ['Shashikant', 3]]
append_values(execl_file_path, "Sheet1", new_values)
