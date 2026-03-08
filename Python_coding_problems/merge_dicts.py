# File: merge_dicts.py
# Problem: Merge two dictionaries manually

def merge_dicts(dict1, dict2):
    merged = {}
    # Copy elements from dict1
    for key in dict1:
        merged[key] = dict1[key]
    # Copy elements from dict2
    for key in dict2:
        merged[key] = dict2[key]
    return merged

def main():
    # Input from standard input
    print("Enter first dictionary (key:value pairs separated by space):")
    dict1_input = input().split()
    dict1 = {}
    for pair in dict1_input:
        key, value = pair.split(":")
        dict1[key] = value

    print("Enter second dictionary (key:value pairs separated by space):")
    dict2_input = input().split()
    dict2 = {}
    for pair in dict2_input:
        key, value = pair.split(":")
        dict2[key] = value

    # Process
    result = merge_dicts(dict1, dict2)

    # Output
    print("Merged Dictionary:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python merge_dicts.py
Enter first dictionary (key:value pairs separated by space):
a:1 b:2
Enter second dictionary (key:value pairs separated by space):
c:3 d:4
Merged Dictionary:
{'a': '1', 'b': '2', 'c': '3', 'd': '4'}
