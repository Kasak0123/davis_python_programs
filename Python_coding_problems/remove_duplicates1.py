# File: remove_duplicates1.py
# Problem: Remove duplicate characters from string

def remove_duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    result = remove_duplicates(user_input)

    # Output
    print("String after removing duplicate characters:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python remove_duplicates1.py
Enter a string:
programming
String after removing duplicate characters:
progamin
