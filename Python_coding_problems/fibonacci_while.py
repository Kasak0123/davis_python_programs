# fibonacci_while.py

# Read input from standard input
N = int(input())

# Initialize first two terms
a, b = 0, 1
count = 0

# Generate Fibonacci series using while loop
while count < N:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python fibonacci_while.py
7
0 1 1 2 3 5 8 
