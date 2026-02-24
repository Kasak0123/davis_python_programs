# File: rotate_list.py
# Problem: Rotate a list by K positions

# Input Format:
# First line: list elements
# Second line: integer K (number of positions to rotate)
# Example:
# 10 20 30 40 50
# 2

numbers = list(map(int, input().split()))
k = int(input())

# Normalize K to avoid unnecessary rotations
k = k % len(numbers)

# Rotate list by slicing
rotated_list = numbers[-k:] + numbers[:-k]

# Output Format: Print the required output
print(*rotated_list)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python rotate_list.py
10 20 30 40 50
2
40 50 10 20 30
