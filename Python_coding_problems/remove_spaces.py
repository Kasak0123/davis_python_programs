# File: remove_spaces.py
# Problem: Remove spaces from string

def remove_spaces(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input()

    # Process
    result = remove_spaces(user_input)

    # Output
    print("String without spaces:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python remove_spaces.py
Enter a string:
python is powerful
String without spaces:
pythonispowerful
