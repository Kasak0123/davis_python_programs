# File: largest_in_list.py
# Problem: Find largest element in a list

# Input Format: Read list elements from standard input
# Example: 10 25 3 47 15
numbers = list(map(int, input().split()))

# Initialize largest with the first element
largest = numbers[0]

# Traverse the list to find the largest element
for num in numbers:
    if num > largest:
        largest = num

# Output Format: Print the required output
print(largest)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python largest_in_list.py
20 47 23 5 40
47
