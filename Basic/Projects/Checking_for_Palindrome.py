# Prompt the user to enter a number
number = input("Enter a number: ")

# Check if the number is a palindrome by comparing it to its reverse
if number == number[::-1]:
    # If the number is the same forwards and backwards, it is a palindrome
    print(f"{number} is a palindrome")
else:
    # If the number is not the same forwards and backwards, it is not a palindrome
    print(f"{number} is not a palindrome")

# ------------------------------- Output -------------------------------- #
# Case 1:
# Enter a number: 121
# 121 is a palindrome

# Case 2:
# Enter a number: 123
# 123 is not a palindrome
