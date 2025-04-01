import os

path1 = 'Advanced/Managing Files and Directories/Text Files/file1.txt'
path2 = 'Advanced/Managing Files and Directories/Text Files/file2.txt'

if os.path.samefile(path1, path2):
    print(f"{path1} and {path2} are the same file.")
else:
    print(f"{path1} and {path2} are different files.")
    
