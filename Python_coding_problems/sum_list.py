# File: sum_list.py
# Problem: Find sum of list elements

# Input Format: Read list elements from standard input
# Example: 10 20 30 40 50
numbers = list(map(int, input().split()))

# Calculate sum manually (without using built-in sum)
total = 0
for num in numbers:
    total += num

# Output Format: Print the required output
print(total)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sum_list.py
10 20 30 40 50
150
