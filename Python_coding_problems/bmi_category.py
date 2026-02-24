# Read input from standard input
# Input format: weight (kg) and height (m) separated by space
weight, height = map(float, input().split())

# Calculate BMI
bmi = weight / (height ** 2)

# Determine category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python bmi_category.py
75 1.75
Normal weight
