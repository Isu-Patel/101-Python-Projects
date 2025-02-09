s = input("Enter a string to repeat: ")
repeat_count = int(input("How many times would you like to repeat it? "))
if repeat_count < 0:
    print("Please enter a non-negative number.")
else:
    repeated_string = (s + " ") * repeat_count
    print(repeated_string)
