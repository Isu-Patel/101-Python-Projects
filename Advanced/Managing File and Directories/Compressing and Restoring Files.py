import zipfile

with zipfile.ZipFile("archive.zip", 'w') as zipf:
    zipf.write("D:\\101 Python Course 2025\\Advanced\\Managing Files and Directories\\Text Files\\file1.txt", "file1.txt")
    zipf.write("D:\\101 Python Course 2025\\Advanced\\Managing Files and Directories\\Text Files\\file2.txt", "file2.txt")
    
    
with zipfile.ZipFile("archive.zip", 'r') as zipf:
    zipf.extractall("D:\\101 Python Course 2025\\Advanced\\Managing Files and Directories\\Text Files\\Extracted")
