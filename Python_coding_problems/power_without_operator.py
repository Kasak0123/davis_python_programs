# power_without_operator.py

# Read input from standard input
base, exponent = map(int, input().split())

# Initialize result
result = 1

# Calculate power without using exponent operator
for i in range(exponent):
    result *= base

# Print the result
print(result)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python power_without_operator.py
2 5
32
