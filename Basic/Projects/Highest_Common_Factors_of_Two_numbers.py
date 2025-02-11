def hcf(a, b):
    """
    This function calculates the Highest Common Factor (HCF) of two numbers using the Euclidean Algorithm.
    """
    # While b is not zero
    while b:
        # Swap the values of a and b
        a, b = b, a % b
    # Return the HCF
    return a

# Prompt the user to enter the first number
number1 = int(input("Enter the first number: "))

# Prompt the user to enter the second number
number2 = int(input("Enter the second number: "))

# Print the HCF of the two numbers
print(f"The HCF of {number1} and {number2} is {hcf(number1, number2)}")

# ------------------------- Output ------------------------------- #
# Enter the first number: 12
# Enter the second number: 18
# The HCF of 12 and 18 is 6.
