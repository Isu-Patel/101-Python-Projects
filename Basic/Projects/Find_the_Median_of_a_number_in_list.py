# Prompt the user to enter numbers separated by spaces and convert them to a sorted list of integers
numbers = sorted(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate the number of elements in the list
n = len(numbers)

# Determine and calculate the median based on whether the number of elements is even or odd
if n % 2 == 0:
    # If even, the median is the average of the two middle elements
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    # If odd, the median is the middle element
    median = numbers[n // 2]

# Print the calculated median
print(f"The median of the list is: {median}")

# ---------------------------- Output ---------------------------- #
# Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9 10
# The median of the list is: 5.5
