# count_digits.py

# Read input from standard input
num = int(input())

# Handle zero separately
if num == 0:
    print(1)
else:
    count = 0
    # Work with absolute value to handle negatives
    num = abs(num)
    
    # Count digits using while loop
    while num > 0:
        num //= 10
        count += 1
    
    # Print the result
    print(count)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python count_digits.py
12345
5
