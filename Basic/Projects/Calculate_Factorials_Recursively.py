def factorial(n):
    # Raise an error if the input is a negative number
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Prompt the user to enter a number
num = int(input("Enter a number to calculate its factorial: "))
# Print the factorial of the entered number
print(f"The factorial of {num} is {factorial(num)}")

# ------------------------------- Output -------------------------------- #
# Case 1:
# Enter a number to calculate its factorial: 5
# The factorial of 5 is 120

# Case 2:
# Enter a number to calculate its factorial: 0
# The factorial of 0 is 1
