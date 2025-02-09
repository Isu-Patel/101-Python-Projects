# Prompt the user to enter the number of terms for the Fibonacci sequence
n = int(input("Enter the number of terms:"))

# Initialize the first two terms of the Fibonacci sequence
f1, f2 = 0, 1

# Print the header for the Fibonacci sequence output
print("Fibonacci Sequence: ")

# Loop through the range of the number of terms
for i in range(n):
    # Print the current term in the sequence
    print(f1, end=" ")
    # Update the values of f1 and f2 to the next terms in the sequence
    f1, f2 = f2, f1 + f2

# ------------------------- Output --------------------------------
# Enter the number of terms: 10
# Fibonacci Sequence:
# 0 1 1 2 3 5 8 13 21 34
