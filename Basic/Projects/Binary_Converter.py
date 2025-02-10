# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Convert the number to its binary representation
binary = bin(num)

# Convert the number to its octal representation
octal = oct(num)

# Convert the number to its hexadecimal representation
hexadecimal = hex(num)

# Print the binary representation of the number
print(f"The binary representation of {num} is {binary}")

# Print the octal representation of the number
print(f"The octal representation of {num} is {octal}")

# Print the hexadecimal representation of the number
print(f"The hexadecimal representation of {num} is {hexadecimal}")

# ------------------------- Output ------------------------------- #
# Enter a number: 10
# The binary representation of 10 is 0b1010
# The octal representation of 10 is 0o12
# The hexadecimal representation of 10 is 0xa
