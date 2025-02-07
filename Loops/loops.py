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


for num in range(10):  # 0 to 9
    print(num)
