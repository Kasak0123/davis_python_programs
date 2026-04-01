# swap_dict.py

def swap_keys_values(original_dict):
    swapped = {}
    for key, value in original_dict.items():
        swapped[value] = key
    return swapped


# Example usage
if __name__ == "__main__":
    data = {"a": 1, "b": 2, "c": 3}
    result = swap_keys_values(data)
    print("Swapped dictionary:", result)
