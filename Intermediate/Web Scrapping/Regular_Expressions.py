import re

# ---------------------- Program 1 ---------------------- #

# Define a regular expression pattern to match strings that start with 'Hello'
pattern = "^Hello"

# Define the string to be checked against the pattern
string = "Hello, World!"

# Use re.match() to check if the string starts with the pattern
if re.match(pattern, string):
    # If a match is found, print a success message
    print("Match found!")
else:
    # If no match is found, print a failure message
    print("No match found.")

# ---------------------------- Output ---------------------------- #
# Match found! 

# ----------------------- Program 2 ---------------------- #

# Find all occurrences of words that start with 'p' in the given string
pattern = r"\bp\w+"  # Matches words that start with 'p'
string = "python is a great programming language. Let's Learn more about it!"

# Use re.findall() to find all occurrences of the pattern in the string
matches = re.findall(pattern, string)
print(" Matches Found: ", matches)

# ---------------------------- Output ---------------------------- #
#  Matches Found:  ['python', 'programming']

# ---------------------------- Output ---------------------------- #
#  Matches Found:  ['python', 'programming', 'language']

# ----------------------- Program 3 ---------------------- #

# Replace all the digits in the string with '###'
pattern = r"\d+"  # Matches one or more digits
string = "my phone number is 123-456-7890"

# Use re.sub() to replace all occurrences of the pattern with '###'
replaced_string = re.sub(pattern, "###", string)
print(replaced_string)

# ---------------------------- Output ---------------------------- #
# my phone number is ###-###-####
