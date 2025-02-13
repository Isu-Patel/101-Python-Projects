# Try to get two numbers from the user and divide them
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
# If the user enters zero for the denominator, print a nice message
except ZeroDivisionError:
    print("You can't divide by zero!")
# If the user enters something that can't be converted to an integer, print a nice message
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# If no errors occur, print the result
else:
    print(f"The result is {result}")
# Always print this message, even if there was an error
finally:
    print("Executing finally clause")

# ---------------------------- Output ---------------------------- #

# -- Case 1 -- #
# Enter the numerator: 10
# Enter the denominator: 0
# You can't divide by zero!
# Executing finally clause

# -- Case 2 -- #
# Enter the numerator: 10
# Enter the denominator: 2
# The result is 5.0
# Executing finally clause

# -- Case 3 -- #
# Enter the numerator: 10
# Enter the denominator: a
# Numerator and denominator must be valid numbers!
# Executing finally clause
