# remove_duplicates.py

def remove_duplicates(numbers):
    unique_list = []
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


# Example usage
if __name__ == "__main__":
    data = [1, 2, 2, 3, 4, 3, 5, 1]
    result = remove_duplicates(data)
    print("List without duplicates:", result)
