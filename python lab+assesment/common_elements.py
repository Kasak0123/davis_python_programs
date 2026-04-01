# common_elements.py

def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common


# Example usage
if __name__ == "__main__":
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = find_common_elements(list_a, list_b)
    print("Common elements:", result)
