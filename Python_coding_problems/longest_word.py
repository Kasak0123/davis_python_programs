# File: longest_word.py
# Problem: Find longest word in a sentence

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def main():
    # Input from standard input
    print("Enter a sentence:")
    user_input = input().strip()

    # Process
    longest_word = find_longest_word(user_input)

    # Output
    print("Longest word in the sentence:")
    print(longest_word)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python longest_word.py
Enter a sentence:
Python is a powerful programming language
Longest word in the sentence:
programming
