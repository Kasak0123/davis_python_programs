# File: replace_vowels.py
# Problem: Replace all vowels with *

def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input()

    # Process
    result = replace_vowels(user_input)

    # Output
    print("String after replacing vowels:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python replace_vowels.py
Enter a string:
Hello World
String after replacing vowels:
H*ll* W*rld
