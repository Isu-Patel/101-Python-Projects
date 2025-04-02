import tarfile

with tarfile.open("archive.tar", 'w') as tar:
    tar.add("D:\\101 Python Course 2025\\Advanced\\Managing Files and Directories\\Files\\file1.txt", "file1.txt")
    tar.add("D:\\101 Python Course 2025\\Advanced\\Managing Files and Directories\\Files\\file2.txt", "file2.txt")

with tarfile.open('archive.tar', 'r') as tar:
    tar.extractall("D:\\101 Python Course 2025\\Advanced\\Managing Files and Directories\\Files\\Extracted")