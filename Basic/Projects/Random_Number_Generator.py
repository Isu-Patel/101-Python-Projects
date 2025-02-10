import random  # Import the random module to generate random numbers

# Prompt the user to enter the lower bound and convert it to an integer
low = int(input("Enter the lower bound: "))

# Prompt the user to enter the upper bound and convert it to an integer
high = int(input("Enter the upper bound: "))

# Generate a random number between the lower and upper bounds (inclusive)
random_number = random.randint(low, high)

# Print the generated random number along with the bounds
print(f"The random number between {low} and {high} is: {random_number}")

# ------------------------- Output ------------------------------- #
# Enter the lower bound: 1
# Enter the upper bound: 100
# The random number between 1 and 100 is: 73
