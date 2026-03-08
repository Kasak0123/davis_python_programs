# File: char_frequency1.py
# Problem: Find frequency of each character in string

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    result = char_frequency(user_input)

    # Output
    print("Character frequencies:")
    for char, count in result.items():
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python char_frequency1.py
Enter a string:
Hello
Character frequencies:
H: 1
e: 1
l: 2
o: 1
