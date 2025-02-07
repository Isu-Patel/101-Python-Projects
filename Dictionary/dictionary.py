dictionary = {} # Dictionary is stored in a querly brackets and it is a key value pair

# Creating a dictionary with initial key-value pairs
student = {'Name': 'Isu', 'Age': 20}

# Adding a new key-value pair to the dictionary
student['Address'] = 'Gujrat'

# Printing the entire dictionary
print(student)

# Printing the value associated with the key 'Name'
print("\n-> Printing the value associated with the key 'Name'")

print(student['Name'])

# Printing the value associated with the key 'Age'
print("\n-> Printing the value associated with the key 'Age'")

print(student['Age'])

# Checking whether del function is working in dictionary or not
print("\n-> Checking whether del function is working in dictionary or not")

del student['Name']
print(student)

# Printing all the keys and values in the dictionary
print("\n-> Printing all the keys and values in the dictionary")

print(student.keys())
print(student.values())

# Checking for if statement
print("\n-> Checking for if statement")

if "Age" in student:
    print("Age is present in the dictionary")
