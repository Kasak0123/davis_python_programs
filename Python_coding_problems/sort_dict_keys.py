# File: sort_dict_keys.py
# Problem: Sort dictionary by keys

def sort_dict_by_keys(d):
    # Sort keys and build a new dictionary
    sorted_dict = {}
    for key in sorted(d.keys()):
        sorted_dict[key] = d[key]
    return sorted_dict

def main():
    # Input from standard input
    print("Enter dictionary (key:value pairs separated by space):")
    dict_input = input().split()
    d = {}
    for pair in dict_input:
        key, value = pair.split(":")
        d[key] = value

    # Process
    result = sort_dict_by_keys(d)

    # Output
    print("Dictionary sorted by keys:")
    print(result)

if __name__ == "__main__":
    main()
## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sort_dict_keys.py
Enter dictionary (key:value pairs separated by space):
b:2 a:1 c:3
Dictionary sorted by keys:
{'a': '1', 'b': '2', 'c': '3'}
