# factorial_while.py

# Read input from standard input
N = int(input())

# Initialize factorial
fact = 1
i = 1

# Calculate factorial using while loop
while i <= N:
    fact *= i
    i += 1

# Print the result
print(fact)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python factorial_while.py
5
120
