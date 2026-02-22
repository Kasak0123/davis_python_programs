# Function to check palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Print palindrome numbers between 1 and 200
for i in range(1, 201):
    if is_palindrome(i):
        print(i, end=" ")