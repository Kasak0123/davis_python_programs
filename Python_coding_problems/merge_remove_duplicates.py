# File: merge_remove_duplicates.py
# Problem: Merge two lists and remove duplicates

# Input Format: Read two lists from standard input
# Example:
# First line: 10 20 30 40
# Second line: 30 40 50 60
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Merge the two lists
merged_list = list1 + list2

# Remove duplicates using a set, then convert back to list
unique_list = list(set(merged_list))

# Output Format: Print the required output
print(*unique_list)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python merge_remove_duplicates.py
10 20 30 40
30 40 50 60
40 10 50 20 60 30
