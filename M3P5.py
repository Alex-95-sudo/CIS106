# Set the value of pi
pi = 3.14

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate radius squared
radius_squared = radius * radius

# Calculate the area
area = pi * radius_squared

# Calculate the perimeter
perimeter = 2 * pi * radius

# Display the results
print("Area of the circle: {:.2f}".format(area))
print("Perimeter of the circle: {:.2f}".format(perimeter))