# max_of_three.py

# Function to find maximum of three numbers
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Read input from standard input
a, b, c = map(int, input().split())

# Print the result
print(maximum(a, b, c))
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python max_of_three.py
12 45 23
45
