# Read input from standard input
P, R, T = map(float, input().split())

# Calculate Compound Interest
CI = P * ((1 + R / 100) ** T) - P

# Print the result
print(CI)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python compound_interest.py
1000 5 2
102.5
