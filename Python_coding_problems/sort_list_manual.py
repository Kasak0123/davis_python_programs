# File: sort_list_manual.py
# Problem: Sort a list without using sort method

# Input Format: Read list elements from standard input
# Example: 12 4 56 7 23
numbers = list(map(int, input().split()))

# Implement Bubble Sort
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Output Format: Print the required output
print(*numbers)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sort_list_manual.py
12 4 56 7 23
4 7 12 23 56
