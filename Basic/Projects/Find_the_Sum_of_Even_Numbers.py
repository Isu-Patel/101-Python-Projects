# Prompt the user to enter numbers separated by spaces and convert them to a list of integers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate the sum of the even numbers in the list
even_sum = sum(num for num in numbers if num % 2 == 0)

# Print the sum of the even numbers
print(f"The sum of even numbers in the list is: {even_sum}")

# ---------------------------- Output ---------------------------- #
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9 10
# The sum of even numbers in the list is: 30
