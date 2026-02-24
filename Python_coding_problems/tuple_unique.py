# File: tuple_unique.py
# Problem: Check whether tuple elements are unique

# Input Format: Read tuple elements from standard input
# Example: 10 20 30 40
numbers = tuple(map(int, input().split()))

# Check uniqueness using set
if len(numbers) == len(set(numbers)):
    print("Unique")
else:
    print("Not Unique")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python tuple_unique.py
10 20 30 40
Unique
