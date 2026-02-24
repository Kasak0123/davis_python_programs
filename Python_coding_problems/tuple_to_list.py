# File: tuple_to_list.py
# Problem: Convert tuple to list

# Input Format: Read tuple elements from standard input
# Example: 10 20 30 40
numbers = tuple(map(int, input().split()))

# Convert tuple to list
converted_list = list(numbers)

# Output Format: Print the required output
print(converted_list)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python tuple_to_list.py
10 20 30 40
[10, 20, 30, 40]
