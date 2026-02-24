# Problem: Calculate power using recursive function

def power(base, exp):
    # Base case
    if exp == 0:
        return 1
    # Recursive case
    return base * power(base, exp - 1)

# Input Format: Read two integers from standard input
base, exp = map(int, input().split())

# Output Format: Print the required output
print(power(base, exp))

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python power_recursive51.py
2 5
32
