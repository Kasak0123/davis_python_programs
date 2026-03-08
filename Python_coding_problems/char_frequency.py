# File: char_frequency.py
# Problem: Count character frequency using dictionary

def count_char_frequency(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

def main():
    # Input from standard input
    user_input = input("Enter a string: ")

    # Process
    result = count_char_frequency(user_input)

    # Output
    print("Character Frequency:")
    for char, freq in result.items():
        print(f"{char}: {freq}")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python char_frequency.py
Enter a string: Hello
Character Frequency:
H: 1
e: 1
l: 2
o: 1
