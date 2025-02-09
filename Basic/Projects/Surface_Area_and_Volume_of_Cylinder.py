import math
# Get input from the user for radius and height
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the volume and surface area of the cylinder
volume = math.pi * radius ** 2 * height
surface_area = 2 * math.pi * radius * (radius + height)

# Displaying the results as per given radius and height
print("Volume of the Cylinder is:", round(volume, 2))
print("Surface Area of the Cylinder is:", round(surface_area, 2))

# ---------------------------- Output ---------------------------- #
# Enter the radius of the cylinder: 5
# Enter the height of the cylinder: 6
# Volume of the Cylinder is: 471.24
# Surface Area of the Cylinder is: 251.33
