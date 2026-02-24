# File: set_difference.py
# Problem: Perform difference of two sets

# Input Format:
# First line: elements of first set
# Second line: elements of second set
# Example:
# 10 20 30
# 30 40 50
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Perform difference (elements in set1 but not in set2)
difference_set = set1 - set2   # or set1.difference(set2)

# Output Format: Print the required output
print(*difference_set)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python set_difference.py
10 20 30
30 40 50
10 20
