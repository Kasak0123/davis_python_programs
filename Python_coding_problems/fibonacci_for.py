# fibonacci_for.py

# Read input from standard input
N = int(input())

# Initialize first two terms
a, b = 0, 1

# Generate Fibonacci series using for loop
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
  ## output
  PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python fibonacci_for.py
7
0 1 1 2 3 5 8 
