# Prompt the user to enter the first string
str1 = input("Enter the first string: ")

# Prompt the user to enter the second string
str2 = input("Enter the second string: ")

# Check if the sorted characters of both strings are equal
if sorted(str1) == sorted(str2):
    # If they are equal, the strings are anagrams
    print("The Strings are Anagrams.")
else:
    # If they are not equal, the strings are not anagrams
    print("The Strings are not Anagrams.")

# ---------------------------- Output ---------------------------- #
# Enter the first string: silent
# Enter the second string: listen
# The Strings are Anagrams.
