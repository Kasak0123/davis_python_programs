# Count character frequency using dictionary

# Step 1: Read input
text = input().strip()

# Step 2: Initialize dictionary
freq = {}

# Step 3: Traverse characters
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Step 4: Print output
for key, value in freq.items():
    print(f"{key}: {value}")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python character_frequency.py
hello
h: 1
e: 1
l: 2
o: 1
