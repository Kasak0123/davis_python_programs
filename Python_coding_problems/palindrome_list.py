# File: palindrome_list.py
# Problem: Check whether list is palindrome

# Input Format: Read list elements from standard input
# Example: 1 2 3 2 1
numbers = list(map(int, input().split()))

# Check if list is palindrome
if numbers == numbers[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python palindrome_list.py
1 2 3 2 1
Palindrome
