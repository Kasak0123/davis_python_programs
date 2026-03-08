# File: dict_from_lists.py
# Problem: Create dictionary from two lists

def create_dict(keys, values):
    # Zip keys and values together into a dictionary
    result = {}
    for i in range(min(len(keys), len(values))):
        result[keys[i]] = values[i]
    return result

def main():
    # Input from standard input
    print("Enter list of keys (space separated):")
    keys = input().split()

    print("Enter list of values (space separated):")
    values = input().split()

    # Process
    result = create_dict(keys, values)

    # Output
    print("Dictionary created from two lists:")
    print(result)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python dict_from_lists.py
Enter list of keys (space separated):
Keys: a b c  
Enter list of values (space separated):
Values: 1 2 3
Dictionary created from two lists:
{'Keys:': 'Values:', 'a': '1', 'b': '2', 'c': '3'}
