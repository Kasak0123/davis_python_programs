# reverse_string.py

# Read input from standard input
text = input()

# Initialize reversed string
rev = ""

# Reverse the string using for loop
for ch in text:
    rev = ch + rev

# Print the result
print(rev)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python reverse_string.py
Hello
olleH
