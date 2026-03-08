# File: check_anagram.py
# Problem: Check whether two strings are anagrams

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for fair comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(str1) == sorted(str2)

def main():
    # Input from standard input
    print("Enter first string:")
    s1 = input().strip()

    print("Enter second string:")
    s2 = input().strip()

    # Process
    if are_anagrams(s1, s2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python check_anagram.py
Enter first string:
Silent
Enter second string:
Listen
The strings are anagrams.
