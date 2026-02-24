# File: separate_even_odd.py
# Problem: Separate even and odd numbers from list

# Input Format: Read list elements from standard input
# Example: 10 21 32 43 54 65
numbers = list(map(int, input().split()))

# Separate even and odd numbers
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Output Format: Print the required output
print("Even:", *even_numbers)
print("Odd:", *odd_numbers)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python seperate_even_odd.py
10 21 32 43 54 65
Even: 10 32 54
Odd: 21 43 65
