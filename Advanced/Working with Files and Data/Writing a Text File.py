
def write_to_text_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        

txt_file_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\sample.txt"
content =  "Hello, this is a sample text file.\nThis is the second line."
write_to_text_file(txt_file_path, content)
