# Program to check valid triangle sides

# Input sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Triangle inequality theorem:
# For a valid triangle, sum of any two sides must be greater than the third side
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a valid triangle.")
else:
    print("Invalid triangle sides.")