def lcm(x, y):
    # Find the greater number between x and y
    greater = max(x, y)
    
    # Loop until we find a number that is divisible by both x and y
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

# Prompt the user to enter the first number
a = int(input("Enter the first number: "))

# Prompt the user to enter the second number
b = int(input("Enter the second number: "))

# Calculate and print the Least Common Multiple of the two numbers
print(f"The Least Common Multiple of {a} and {b} is {lcm(a, b)}")

# ------------------------- Output -------------------------------
# Enter the first number: 4
# Enter the second number: 6
# The Least Common Multiple of 4 and 6 is 12
