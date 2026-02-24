# factorial_function.py

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Read input from standard input
N = int(input())

# Print the result
print(factorial(N))
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python factorial_function.py
5
120
