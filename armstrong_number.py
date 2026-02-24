# armstrong_number.py

# Read input from standard input
num = int(input())

# Convert number to string to count digits
num_str = str(num)
num_digits = len(num_str)

# Calculate sum of digits raised to power of number of digits
sum_of_powers = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

# Check Armstrong condition
if sum_of_powers == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python armstrong_number.py
153
Armstrong Number
