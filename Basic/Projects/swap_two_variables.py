# Take two numbers as input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swap the two numbers using tuple packing and unpacking
a, b = b, a

# Print the swapped numbers
print(f"After swapping: a = {a}, b = {b}")

# ------------------------- Output ------------------------------- #
# Enter the first number: 5
# Enter the second number: 10
# After swapping: a = 10, b = 5
