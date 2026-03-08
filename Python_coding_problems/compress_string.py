# File: compress_string.py
# Problem: Compress a string using character counts

def compress_string(s):
    if not s:
        return ""

    compressed = ""
    count = 1

    # Traverse the string
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1
    # Add the last character group
    compressed += s[-1] + str(count)

    return compressed

def main():
    # Input from standard input
    print("Enter a string:")
    user_input = input().strip()

    # Process
    result = compress_string(user_input)

    # Output
    print("Compressed string:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python compress_string.py
Enter a string:
aaabbc
Compressed string:
a3b2c1
