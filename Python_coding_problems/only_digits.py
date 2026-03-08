# File: only_digits.py
# Problem: Check whether string contains only digits

def contains_only_digits(s):
    # Check each character manually
    for char in s:
        if not char.isdigit():
            return False
    return True

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    if contains_only_digits(user_input):
        print("The string contains only digits.")
    else:
        print("The string does not contain only digits.")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python only_digits.py
Enter a string:
12345
The string contains only digits.
