# File: set_intersection.py
# Problem: Perform intersection of two sets

# Input Format:
# First line: elements of first set
# Second line: elements of second set
# Example:
# 10 20 30
# 30 40 50
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Perform intersection
intersection_set = set1 & set2   # or set1.intersection(set2)

# Output Format: Print the required output
print(*intersection_set)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python set_intersection.py
10 20 30
30 40 50
30
