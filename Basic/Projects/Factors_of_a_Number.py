# Prompt the user to enter a number
num = int(input("Enter a number:"))

# Print the header for the factors
print(f"The factors of {num} are: ")

# Iterate through all numbers from 1 to the entered number
for i in range(1, num + 1):
    # Check if the current number is a factor of the entered number
    if num % i == 0:
        # Print the factor
        print(i, end=" ")

# ------------------------- Output ------------------------------- #
# Enter a number: 12
# The factors of 12 are:
# 1 2 3 4 6 12
