# Program to check valid triangle angles

# Input angles
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

# Validation
if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("The angles form a valid triangle.")
else:
    print("Invalid triangle angles.")