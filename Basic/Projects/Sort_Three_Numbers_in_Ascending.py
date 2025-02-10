# Prompt the user to enter the first number and convert it to an integer
a = int(input("Enter the first number: "))

# Prompt the user to enter the second number and convert it to an integer
b = int(input("Enter the second number: "))

# Prompt the user to enter the third number and convert it to an integer
c = int(input("Enter the third number: "))

# Compare the first and second numbers and swap them if necessary
if a > b:
    a, b = b, a

# Compare the first and third numbers and swap them if necessary
if a > c:
    a, c = c, a

# Compare the second and third numbers and swap them if necessary
if b > c:
    b, c = c, b

# Check if all numbers are equal and print a message if they are
if a == b == c:
    print("All numbers are equal.")
else:
    # Print the numbers in ascending order
    print("After Sorting the numbers would arrange as", a, b, c)

# ------------------------- Output --------------------------------
# Enter the first number: 5
# Enter the second number: 3
# Enter the third number: 7
# After Sorting the numbers would arrange as 3 5 7
