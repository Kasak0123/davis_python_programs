# first_non_repeating.py

def first_non_repeating_char(text):
    # Dictionary to store character counts
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Find the first character with count = 1
    for char in text:
        if freq[char] == 1:
            return char
    return None  # If no non-repeating character exists


# Example usage
if __name__ == "__main__":
    sample_string = "swiss"
    result = first_non_repeating_char(sample_string)
    if result:
        print("First non-repeating character:", result)
    else:
        print("No non-repeating character found.")
