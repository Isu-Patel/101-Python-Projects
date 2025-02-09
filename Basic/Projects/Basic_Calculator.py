# Displays a basic calculator that can add, subtract, multiply, and divide two numbers.
print("Welcome to the Basic Calculator!")
print("Choose an operation:")
print("   1. Addition")
print("   2. Subtraction")
print("   3. Multiplication")
print("   4. Division")

# Get the user's choice
choice = input("Choose an Operation - (1/2/3/4): ")

# Get the numbers from the user
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

# Perform the operation based on the user's choice
if choice == "1":
    result = n1 + n2
    print(f"The sum of {n1} and {n2} is {result}")
elif choice == "2":
    result = n1 - n2
    print(f"The difference of {n1} and {n2} is {result}")
elif choice == "3":
    result = n1 * n2
    print(f"The product of {n1} and {n2} is {result}")
elif choice == "4":
    if n2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = n1 / n2
        print(f"The division of {n1} and {n2} is {result}")
else:
    print("Invalid choice! Please choose a valid operation.")

# ------------------------------- Output -------------------------------- #
# Welcome to the Basic Calculator!
# Choose an operation:
#    1. Addition
#    2. Subtraction
#    3. Multiplication
#    4. Division
# Choose an Operation - (1/2/3/4): 3
# Enter the first number: 5
# Enter the second number: 10
# The product of 5.0 and 10.0 is 50.0
