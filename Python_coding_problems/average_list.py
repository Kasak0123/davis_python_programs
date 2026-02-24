# File: average_list.py
# Problem: Find average of list elements

# Input Format: Read list elements from standard input
# Example: 10 20 30 40 50
numbers = list(map(int, input().split()))

# Calculate sum manually
total = 0
for num in numbers:
    total += num

# Calculate average
average = total / len(numbers)

# Output Format: Print the required output
print(average)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python average_list.py
10 20 30 40 50
30.0
