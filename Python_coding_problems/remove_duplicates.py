# File: remove_duplicates.py
# Problem: Remove duplicate elements from list

# Input Format: Read list elements from standard input
# Example: 10 20 10 30 20 40
numbers = list(map(int, input().split()))

# Use a set to track seen elements
unique_list = []
seen = set()

for num in numbers:
    if num not in seen:
        unique_list.append(num)
        seen.add(num)

# Output Format: Print the required output
print(*unique_list)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python remove_duplicates.py
10 20 10 30 20 40
10 20 30 40
