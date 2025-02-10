def gcd(a, b):
    # Function to compute the Greatest Common Divisor (GCD) using the Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a

# Prompt the user to enter the first number
num1 = int(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = int(input("Enter the second number: "))

# Compute and print the GCD of the two numbers
print(f"The Greatest Common Divisor of {num1} and {num2} is {gcd(num1, num2)}")

# ------------------------- Output -------------------------------- #
# Enter the first number: 12
# Enter the second number: 18
# The Greatest Common Divisor of 12 and 18 is 6
