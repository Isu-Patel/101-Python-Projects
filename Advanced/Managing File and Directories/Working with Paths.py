import os
file_path = os.path.join('Advanced', 'Managing Files and Directories', 'Text Files', 'file.txt')

if os.path.exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")
