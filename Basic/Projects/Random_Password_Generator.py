import string
import random

# Prompt the user to enter the length of the password
length = int(input("Enter the length of the password: "))

# Define the characters to be used in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password by randomly selecting 'length' number of characters
# from the defined characters
password = ''.join(random.choice(characters) for _ in range(length))

# Print the generated password
print(f"Generated Password: {password}")

# ------------------------- Output ------------------------------- #
# Enter the length of the password: 12
# Generated Password: !@#Password

