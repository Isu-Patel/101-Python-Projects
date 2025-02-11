# Prompt the user to enter a string
text = input("Enter a string: ")

# Check if the string contains only digits
# The isdigit() method returns True if all characters in the string are digits, otherwise it returns False
if text.isdigit():
    # If the string contains only digits, print a message indicating that
    print("The string contains only digits.")
else:
    # If the string contains non-digit characters, print a message indicating that
    print("The string contains non-digit characters.")

# ------------------------- Output ------------------------------- #
# Enter a string: 123
# The string contains only digits.

# Enter a string: Hello, World!
# The string contains non-digit characters.
