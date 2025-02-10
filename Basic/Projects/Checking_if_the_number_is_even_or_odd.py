# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    # If the number is divisible by 2, it is even
    print(f"{number} is Even.")
else:
    # If the number is not divisible by 2, it is odd
    print(f"{number} is Odd.")

# ---------------------------- Output ---------------------------- #
# Enter a number: 4
# 4 is Even.

# Enter a number: 7
# 7 is Odd.
