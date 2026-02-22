# Program to calculate area and perimeter of a circle

import math  # to use the value of pi

# Input radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter
area = math.pi * radius * radius
perimeter = 2 * math.pi * radius

# Output results
print("Area of the circle:", area)
print("Perimeter (Circumference) of the circle:", perimeter)