# sum_until_zero.py

# Initialize sum
total = 0

# Read numbers until 0 is entered
while True:
    num = int(input())
    if num == 0:
        break
    total += num

# Print the result
print(total)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sum_until_zero.py
5
10
-3
0
12
