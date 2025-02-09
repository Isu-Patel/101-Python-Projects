# This script prompts the user to input the real and imaginary parts of a complex number,
# creates the complex number using the provided inputs, and then prints the complex number.

real = float(input("Enter the real part of the complex number: "))
imaginary = float(input("Enter the imaginary part of the complex number: "))

complex_number = complex(real, imaginary)

print(f"The complex number is: {complex_number}")

# ---------------------- Output ----------------------
# Enter the real part of the complex number: 3
# Enter the imaginary part of the complex number: 4
# The complex number is: (3 + 4j)
