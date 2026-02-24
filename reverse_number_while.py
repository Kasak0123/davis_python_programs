# reverse_number_while.py

# Read input from standard input
num = int(input())

# Initialize reversed number
rev = 0

# Reverse the number using while loop
while num > 0:
    digit = num % 10       # Extract last digit
    rev = rev * 10 + digit # Append digit to reversed number
    num //= 10             # Remove last digit

# Print the result
print(rev)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python reverse_number_while.py
34
43
