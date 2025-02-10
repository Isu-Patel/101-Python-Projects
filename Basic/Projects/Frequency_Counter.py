# Prompt the user to enter a text
text = input("Enter a text: ")

# Initialize an empty dictionary to store the frequency of each character
frequency = {}

# Iterate over each character in the text
for char in text:
    # If the character is already in the dictionary, increment its count
    if char in frequency:
        frequency[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency[char] = 1

# Print the frequency dictionary
print(f"The frequency of each character in the text is: {frequency}")

# Iterate over the dictionary and print each character with its frequency
for char, count in frequency.items():
    print(f"{char}: {count}")
    
# ------------------------- Output ------------------------------- #
# Enter a text: Hello, World!
# The frequency of each character in the text is: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1}
# H: 1
# e: 1
# l: 3
# o: 2
# ,: 1
#  : 1
# W: 1
# r: 1
# d: 1
# !: 1
