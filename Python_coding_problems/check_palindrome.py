# File: check_palindrome.py
# Problem: Check whether string is palindrome

def is_palindrome(s):
    # Reverse string manually
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return s == reversed_str

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    if is_palindrome(user_input):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python check_Palindrome.py
Enter a string:
madam
The string is a palindrome.
