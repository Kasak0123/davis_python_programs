# File: second_largest.py
# Problem: Find second largest number in list

# Input Format: Read list elements from standard input
# Example: 12 45 7 3 19 45
numbers = list(map(int, input().split()))

# Remove duplicates to handle repeated largest values
unique_numbers = list(set(numbers))

# Edge case: if fewer than 2 unique numbers exist
if len(unique_numbers) < 2:
    print("No second largest element")
else:
    # Initialize largest and second largest
    largest = second_largest = float('-inf')

    for num in unique_numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    # Output Format: Print the required output
    print(second_largest)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python second_largest.py
12 45 7 3 19 45
19
