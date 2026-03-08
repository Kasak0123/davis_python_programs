# File: first_non_repeating.py
# Problem: Find first non-repeating character in string

def first_non_repeating(s):
    freq = {}
    # Count frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    result = first_non_repeating(user_input)

    # Output
    if result:
        print("First non-repeating character:")
        print(result)
    else:
        print("No non-repeating character found.")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python first_non_repeating.py
Enter a string:
swiss
First non-repeating character:
w
