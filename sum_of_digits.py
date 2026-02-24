#  Read input from standard input
num = int(input())

# Initialize sum
digit_sum = 0

# Loop to extract digits
while num > 0:
    digit_sum += num % 10   # Add last digit
    num //= 10              # Remove last digit

# Print the result
print(digit_sum)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sum_of_digits.py
123
6
