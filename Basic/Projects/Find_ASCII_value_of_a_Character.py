# This program takes a character as input and prints its ASCII value.

# Prompt the user to enter a character
char = input("Enter a character: ")

# Use the built-in ord() function to get the ASCII value of the entered character
ascii_value = ord(char)

# Print the ASCII value of the entered character
print(f"The ASCII value of '{char}' is: {ascii_value}")

# ------------------------- Output ------------------------------- #
# Enter a character: a
# The ASCII value of 'a' is: 97
