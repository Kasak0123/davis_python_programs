# File: max_in_tuple.py
# Problem: Find maximum value in a tuple

# Input Format: Read tuple elements from standard input
# Example: 12 45 7 3 19
numbers = tuple(map(int, input().split()))

# Find maximum manually (without using max())
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# Output Format: Print the required output
print(maximum)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python max_in_tuple.py
12 45 7 3 19
45
