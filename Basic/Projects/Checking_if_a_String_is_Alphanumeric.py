# Prompt the user to enter a string
text = input("Enter a string: ")

# Check if the entered string is alphanumeric
# The isalnum() method returns True if all characters in the string are alphanumeric, otherwise it returns False
if text.isalnum():
    # If the string is alphanumeric, print a message indicating that
    print(f"{text} is alphanumeric.")
else:
    # If the string is not alphanumeric, print a message indicating that
    print(f"{text} is not alphanumeric.")

# ------------------------- Output ------------------------------- #
# Enter a string: Hello, World!
# Hello, World! is not alphanumeric.
