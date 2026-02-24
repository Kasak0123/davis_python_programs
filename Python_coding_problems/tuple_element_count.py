# File: tuple_element_count.py
# Problem: Count occurrence of element in tuple

# Input Format:
# First line: tuple elements
# Second line: element to count
# Example:
# 10 20 30 20 40 20
# 20

numbers = tuple(map(int, input().split()))
element = int(input())

# Count occurrences manually (without using count())
occurrence = 0
for num in numbers:
    if num == element:
        occurrence += 1

# Output Format: Print the required output
print(occurrence)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python tuple_element_count.py
10 20 30 40
20
1
