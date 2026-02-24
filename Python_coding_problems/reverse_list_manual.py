# File: reverse_list_manual.py
# Problem: Reverse a list without reverse method

# Input Format: Read list elements from standard input
# Example: 10 20 30 40 50
numbers = list(map(int, input().split()))

# Manual reversal using two-pointer approach
start, end = 0, len(numbers) - 1
while start < end:
    # Swap elements
    numbers[start], numbers[end] = numbers[end], numbers[start]
    start += 1
    end -= 1

# Output Format: Print the required output
print(*numbers)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python reverse_list_manual.py
10 20 30 40 50
50 40 30 20 10
