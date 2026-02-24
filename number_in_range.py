# Read input from standard input
num, low, high = map(int, input().split())

# Check if number lies within the range
if low <= num <= high:
    print("Within Range")
else:
    print("Out of Range")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python number_in_range.py
15 10 20
Within Range
