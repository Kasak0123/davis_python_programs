# flatten_list.py

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursively flatten sublist
        else:
            flat_list.append(item)
    return flat_list


# Example usage
if __name__ == "__main__":
    data = [1, [2, 3], [4, [5, 6]], 7]
    result = flatten(data)
    print("Flattened list:", result)
