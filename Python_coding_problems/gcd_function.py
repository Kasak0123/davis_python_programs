# File name: gcd_function.py

# Function to compute GCD using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Read input from standard input
x, y = map(int, input().split())

# Call the function and print result
print(gcd(x, y))

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python gcd_function.py
36 60
12
