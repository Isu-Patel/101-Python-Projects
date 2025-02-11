# Prompt the user to enter numbers separated by spaces and convert them to a list of integers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate the sum of the numbers in the list
total = sum(numbers)

# Print the total sum of the numbers in the list
print(f"The sum of the list is: {total}")

# ---------------------------- Output ---------------------------- #
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9 10
# The sum of the list is: 55
