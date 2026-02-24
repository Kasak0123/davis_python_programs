# sum_even_numbers.py

# Read input from standard input
N = int(input())

# Initialize sum
sum_even = 0
i = 1

# Calculate sum of even numbers up to N
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

# Print the result
print(sum_even)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sum_even_numbers.py
10
30
