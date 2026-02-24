# Read input from standard input
a, b = map(int, input().split())

# Swap using XOR
a = a ^ b
b = a ^ b
a = a ^ b

# Print the result
print(a, b)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python swap_two_numbers.py              
5 10
10 5
