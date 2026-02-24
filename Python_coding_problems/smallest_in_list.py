# File: smallest_in_list.py
# Problem: Find smallest element in a list

# Input Format: Read list elements from standard input
# Example: 12 45 7 3 19
numbers = list(map(int, input().split()))

# Initialize smallest with the first element
smallest = numbers[0]

# Traverse the list to find the smallest element
for num in numbers:
    if num < smallest:
        smallest = num

# Output Format: Print the required output
print(smallest)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python smallest_in_list.py
20 47 5 23
5
