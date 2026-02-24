# Read input from standard input
ch = input().strip()

# Check whether character is digit or alphabet
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Invalid Input")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python digit_or_alphabet.py
a
Alphabet
