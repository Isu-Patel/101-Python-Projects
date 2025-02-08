# --> For loop example
# ~ This loop will iterate 5 times, printing the iteration number each time.
# for i in range(5):
#     print(f"Iteration {i}")

# --> While loop example
# ~ This loop will continue to run as long as count is less than 5.
# count = 0
# while count < 5:
#     print(f"Count {count}")
#     count += 1  # Increment count by 1

# ---------------------- Program 1 : For Loop ---------------------- #
print("---------------------- Program 1 : For Loop ----------------------")

numbers = [6, 4, 2, 3, 9]
sum = 0

for i in numbers:
    sum = sum + i
    print(f"Sum after adding {i} is {sum}")
    
print(f"Total sum is {sum}")

print("\nFunction 2 : For Loop with range function")
for num in range(10):  # 0 to 9
    print(num)

print("\nFunction 3 : For Loop with range and using start to stop function")
for i in range(12, 59, 4):
    print(f"The Numbers are: {i}")


# ---------------------- Program 2 : While Loop ---------------------- #
print("\n---------------------- Program 2 : While Loop ----------------------")

a = 10
sum = 0
i = 1

while i <= a:
    sum = sum + i
    i = i + 1
    print(f"Sum after adding {i} is {sum}")
