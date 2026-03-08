# File: title_case.py
# Problem: Convert string to title case manually

def to_title_case(s):
    words = s.split()
    result = []
    for word in words:
        if len(word) > 0:
            # Capitalize first character, keep rest lowercase
            title_word = word[0].upper() + word[1:].lower()
            result.append(title_word)
    return " ".join(result)

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    result = to_title_case(user_input)

    # Output
    print("String in Title Case:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python title_case.py
Enter a string:
python is POWERFUL
String in Title Case:
Python Is Powerful
