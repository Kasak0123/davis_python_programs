# Read input from standard input
num = int(input())

# Check even or odd using bitwise AND
if (num & 1) == 0:
    print("Even")
else:
    print("Odd")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python even_or_odd.py
5
Odd
