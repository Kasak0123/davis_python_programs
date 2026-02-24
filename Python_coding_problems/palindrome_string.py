# palindrome_string.py

# Function to check palindrome
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase
    return s == s[::-1]

# Read input from standard input
text = input()

# Check and print result
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python palindrome_string.py
Madam
Palindrome
