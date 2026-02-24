# File: set_union.py
# Problem: Perform union of two sets

# Input Format:
# First line: elements of first set
# Second line: elements of second set
# Example:
# 10 20 30
# 30 40 50
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Perform union
union_set = set1 | set2   # or set1.union(set2)

# Output Format: Print the required output
print(*union_set)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python set_union.py
10 20 30
30 40 50
50 20 40 10 30
