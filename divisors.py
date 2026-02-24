# divisors.py

# Read input from standard input
N = int(input())

# Print all divisors of N
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=" ")
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python divisors.py
12
1 2 3 4 6 12 
