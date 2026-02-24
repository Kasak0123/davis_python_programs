# File: set_subset.py
# Problem: Check whether one set is subset of another

# Input Format:
# First line: elements of first set
# Second line: elements of second set
# Example:
# 10 20 30
# 10 20 30 40 50
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Check if set1 is subset of set2
if set1 <= set2:   # or set1.issubset(set2)
    print("Subset")
else:
    print("Not Subset")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python set_subset.py
10 20 30
10 20 30 40 50
Subset
