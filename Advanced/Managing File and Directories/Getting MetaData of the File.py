import os

file_info = os.stat('D:\\101 Python Course 2025\\Advanced\\Managing Files and Directories\\Text Files\\file1.txt')
print('File Size in Bytes:', file_info.st_size, 'bytes')
print('Last Modified Time:', file_info.st_mtime)
