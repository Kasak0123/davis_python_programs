# File name: count_vowels_function.py

# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

# Read input from standard input
text = input()

# Call the function and print result
print(count_vowels(text))

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python count_vowels_function.py
Artificial intelligence
10
