# File: replace_negatives.py
# Problem: Replace negative numbers with zero

# Input Format: Read list elements from standard input
# Example: 10 -5 20 -15 30
numbers = list(map(int, input().split()))

# Replace negative numbers with zero
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

# Output Format: Print the required output
print(*numbers)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python replace_negatives.py
10 -5 20 -15 30
10 0 20 0 30
