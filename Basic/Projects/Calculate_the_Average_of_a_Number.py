# Prompt the user to enter numbers separated by spaces
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate the average of the entered numbers
average = sum(numbers) / len(numbers)

# Print the calculated average
print(f"The average of the entered numbers is: {average}")

# ---------------------------- Output ---------------------------- #
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9 10
# The average of the entered numbers is: 5.5
