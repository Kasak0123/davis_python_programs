# File: count_case.py
# Problem: Count uppercase and lowercase letters

def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    upper, lower = count_case(user_input)

    # Output
    print("Number of uppercase letters:", upper)
    print("Number of lowercase letters:", lower)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python count_case.py
Enter a string:
Hello World
Number of uppercase letters: 2
Number of lowercase letters: 8
