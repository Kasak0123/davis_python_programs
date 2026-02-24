# gcd_while.py

# Read input from standard input
a, b = map(int, input().split())

# Euclidean algorithm using while loop
while b != 0:
    a, b = b, a % b

# Print the result
print(a)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python gcd_while.py
48 18
6
