# Prompt the user to enter a text
texts = input("Enter a text: ")

# Define a string containing all vowels (both lowercase and uppercase)
vowels = 'aeiouAEIOU'

# Count the number of vowels in the input text
count = sum(1 for char in texts if char in vowels)

# Print the number of vowels found in the text
print(f"The number of vowels in the text is: {count}")

# ------------------------- Output ------------------------------- #
# Enter a text: Hello, World!
# The number of vowels in the text is: 3

# Enter a text: PYthon is a programming language
# The number of vowels in the text is: 9
