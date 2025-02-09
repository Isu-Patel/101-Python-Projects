n = int(input("Enter the number of terms:"))
f1, f2 = 0, 1

print("Fibonacci Sequence: ")

for i in range(n):
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2

# ------------------------- Output --------------------------------
# Enter the number of terms: 10
# Fibonacci Sequence:
# 0 1 1 2 3 5 8 13 21 34
