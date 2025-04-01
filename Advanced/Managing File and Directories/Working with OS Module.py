import os

current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

contents = os.listdir(current_dir)
print("Contents of the current directory:", contents)
