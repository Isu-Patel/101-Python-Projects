import math
# Get input from the user for radius
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume and surface area of the sphere
surface_area = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius ** 3

# Displaying the results as per given radius
print(f"Surface Area of the Sphere is {surface_area:.2f}")
print(f"Volume of the Sphere is {volume:.2f}")
