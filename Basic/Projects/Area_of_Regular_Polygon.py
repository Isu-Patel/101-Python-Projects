import math

# Get input from the user for number of sides and length of each side
n = int(input("Enter the number of sides: "))
s = int(input("Enter the length of each side: "))

# Calculate the area of the regular polygon
area = (n * s ** 2) / (4 * math.tan(math.pi / n))

# Displaying the results as per given number of sides and length of each side
print(f"Area of the Regular Polygon is {area:.2f}")

# ---------------------------- Output ---------------------------- #
# Enter the number of sides: 5
# Enter the length of each side: 6
# Area of the Regular Polygon is 61.94
