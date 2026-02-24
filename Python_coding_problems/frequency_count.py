# File: frequency_count.py
# Problem: Count frequency of elements in list

# Input Format: Read list elements from standard input
# Example: 10 20 10 30 20 40 10
numbers = list(map(int, input().split()))

# Dictionary to store frequency
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Output Format: Print the required output
for key, value in frequency.items():
    print(key, value)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python frequency_count.py
10 20 10 30 20 40 10
10 3
20 2
30 1
40 1
