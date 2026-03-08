# File: all_substrings.py
# Problem: Generate all substrings of a string

def generate_substrings(s):
    substrings = []
    n = len(s)
    # Outer loop for start index
    for i in range(n):
        # Inner loop for end index
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    result = generate_substrings(user_input)

    # Output
    print("All substrings of the string:")
    for substring in result:
        print(substring)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python all_substrings.py
Enter a string:
abc
All substrings of the string:
a
ab
abc
b
bc
c
