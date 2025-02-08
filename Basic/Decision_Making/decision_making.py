# --> if statement
# ~ The if statement is used to test a specific condition. If the condition is true, the block of code inside the if statement is executed.
#if x > 10:
#   print("x is greater than 10")  # This block executes if x is greater than 10

# --> if-else statement
# ~ The if-else statement is used to test a specific condition. If the condition is true, the block of code inside the if statement is executed. Otherwise, the block of code inside the else statement is executed.
# if x > 10:
#     print("x is greater than 10")  # This block executes if x is greater than 10
# else:
#     print("x is 10 or less")  # This block executes if x is 10 or less

# --> if-elif-else statement
# ~ The if-elif-else statement is used to test multiple conditions. The block of code inside the if statement is executed if the first condition is true. If the first condition is false, the elif condition is tested. If the elif condition is true, the block of code inside the elif statement is executed. If none of the conditions are true, the block of code inside the else statement is executed.
# if x > 10:
#     print("x is greater than 10")  # This block executes if x is greater than 10
# elif x == 10:
#     print("x is exactly 10")  # This block executes if x is exactly 10
# else:
#     print("x is less than 10")  # This block executes if x is less than 10

# ---------------------- Program 1 : If Statement ---------------------- #
print("---------------------- Program 1 : If Statement ----------------------")

a = 10 

if a > 0:
    print(a ,"is positive number!")
print("This statement is always printed")

# ---------------------- Program 2 : If-Else Statement ---------------------- #/
print("\n---------------------- Program 2 : If-Else Statement ----------------------")

a = 10

if a > 0:
    print("Positive number!")
else:
    print("Negative number!")

# ---------------------- Program 3 : If-Elif-Else Statement ---------------------- #
print("\n---------------------- Program 3 : If-Elif-Else Statement ----------------------")

a = 100 # You can change this to 100 or -100 to test the other condition

if a > 50:
    print("a is greater than 50")
elif a == 10:
    print("a is exactly 10")
else:
    print("a is less than 50 or it's a negative number")
