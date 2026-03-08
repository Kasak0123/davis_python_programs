# File: sort_dict_values.py
# Problem: Sort dictionary by values

def sort_dict_by_values(d):
    # Sort items by value and build a new dictionary
    sorted_dict = {}
    for key, value in sorted(d.items(), key=lambda item: item[1]):
        sorted_dict[key] = value
    return sorted_dict

def main():
    # Input from standard input
    print("Enter dictionary (key:value pairs separated by space):")
    dict_input = input().split()
    d = {}
    for pair in dict_input:
        key, value = pair.split(":")
        # Convert values to int if numeric, else keep as string
        if value.isdigit():
            d[key] = int(value)
        else:
            d[key] = value

    # Process
    result = sort_dict_by_values(d)

    # Output
    print("Dictionary sorted by values:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sort_dict_values.py
Enter dictionary (key:value pairs separated by space):
a:3 b:1 c:2
Dictionary sorted by values:
{'b': 1, 'c': 2, 'a': 3}
