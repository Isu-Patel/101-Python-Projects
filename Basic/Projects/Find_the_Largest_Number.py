# Prompt the user to enter numbers separated by spaces
Numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Find the largest number in the list
largest_number = max(Numbers)

# Print the largest number
print(f"The largest number is: {largest_number}")

# ------------------------- Output ------------------------------- #
# Enter numbers separated by spaces: 10 20 30 40 50 60 70 80 90 100
# The largest number is: 100
