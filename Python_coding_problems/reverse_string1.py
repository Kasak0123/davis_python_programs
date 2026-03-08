# File: reverse_string1.py
# Problem: Reverse a string without slicing

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str   # prepend each character
    return reversed_str

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    result = reverse_string(user_input)

    # Output
    print("Reversed string:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python reverse_string1.py
Enter a string:
Hello
Reversed string:
olleH
