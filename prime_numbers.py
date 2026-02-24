# prime_numbers.py

# Read input from standard input
N = int(input())

# Start from 2 (first prime)
num = 2

# Print prime numbers between 1 and N
while num <= N:
    is_prime = True
    divisor = 2
    
    # Check divisibility
    while divisor <= num // 2:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    
    if is_prime:
        print(num, end=" ")
    
    num += 1
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python prime_numbers.py
20
2 3 5 7 11 13 17 19 
