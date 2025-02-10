# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Calculate the sum of the digits of the number
sum_of_digits = sum(int(digit) for digit in str(num))

# Print the result
print(f"The sum of the digits of {num} is {sum_of_digits}")

# ------------------------- Output ------------------------------- #
# Enter a number: 1234
# The sum of the digits of 1234 is 10
