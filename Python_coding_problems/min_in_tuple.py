# File: min_in_tuple.py
# Problem: Find minimum value in a tuple

# Input Format: Read tuple elements from standard input
# Example: 12 45 7 3 19
numbers = tuple(map(int, input().split()))

# Find minimum manually (without using min())
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

# Output Format: Print the required output
print(minimum)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python min_in_tuple.py
12 45 7 3 19
3
