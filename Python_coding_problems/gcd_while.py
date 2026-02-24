# Program to find GCD using while loop

# Input Format: Read two integers from standard input
a, b = map(int, input().split())

# Using Euclidean Algorithm with while loop
while b != 0:
    a, b = b, a % b

# Output Format: Print the required output
print(a)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python gcd_while.py
20 48
4
