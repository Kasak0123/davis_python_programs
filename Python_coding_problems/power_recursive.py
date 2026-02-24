# Recursive function to calculate power
def power(base, exp):
    # Base case
    if exp == 0:
        return 1
    # Recursive case
    return base * power(base, exp - 1)

# Read input from standard input
base, exp = map(int, input().split())

# Call the function and print result
print(power(base, exp))

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python power_recursive.py
2 5
32
