# count_vowels.py

# Read input from standard input
text = input()

# Initialize vowel count
count = 0

# Convert to lowercase for uniformity
text = text.lower()

# Count vowels using for loop
for ch in text:
    if ch in "aeiou":
        count += 1

# Print the result
print(count)
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python count_vowels.py
Hello World
3
