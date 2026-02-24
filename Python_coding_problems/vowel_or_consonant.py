# Read input from standard input
ch = input().strip().lower()

# Check if character is alphabet
if ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python vowel_or_consonant.py
C
Consonant
