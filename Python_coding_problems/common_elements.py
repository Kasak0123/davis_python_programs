# File: common_elements.py
# Problem: Find common elements between two lists

# Input Format: Read two lists from standard input
# Example:
# First line: 10 20 30 40
# Second line: 30 40 50 60
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Find common elements using set intersection
common = list(set(list1) & set(list2))

# Output Format: Print the required output
print(*common)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python common_elements.py
10 20 30 40
30 40 50 60
40 30
