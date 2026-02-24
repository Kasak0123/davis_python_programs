# prime_function.py

# Function to check prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Read input from standard input
n = int(input())

# Check and print result
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python prime_function.py
29
Prime
