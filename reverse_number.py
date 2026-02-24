# Read input from standard input
num = int(input())

# Initialize reversed number
rev = 0

# Loop to reverse digits
while num > 0:
    digit = num % 10       # Get last digit
    rev = rev * 10 + digit # Append digit to reversed number
    num //= 10             # Remove last digit

# Print the result
print(rev)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python reverse_number.py
123
321
