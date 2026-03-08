# File: count_words.py
# Problem: Count number of words in a sentence

def count_words(sentence):
    # Split sentence by whitespace and count
    words = sentence.split()
    return len(words)

def main():
    # Input from standard input
    print("Enter a sentence:")
    user_input = input().strip()

    # Process
    word_count = count_words(user_input)

    # Output
    print("Number of words in the sentence:")
    print(word_count)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python count_words.py
Enter a sentence:
Python is a powerful language
Number of words in the sentence:
5
