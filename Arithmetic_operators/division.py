# Program to divide two numbers

# Input values
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Division with validation
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print("Result of division:", result)