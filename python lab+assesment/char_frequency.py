# char_frequency.py

def count_char_frequency(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


# Example usage
if __name__ == "__main__":
    sample_string = "hello world"
    result = count_char_frequency(sample_string)
    print("Character frequency dictionary:", result)
