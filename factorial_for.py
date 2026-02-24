# factorial_for.py

# Read input from standard input
N = int(input())

# Initialize factorial
fact = 1

# Calculate factorial using for loop
for i in range(1, N + 1):
    fact *= i

# Print the result
print(fact)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python factorial_for.py
5
120
