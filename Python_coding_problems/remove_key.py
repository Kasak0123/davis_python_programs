# File: remove_key.py
# Problem: Safely remove a key from dictionary

def remove_key(d, key):
    # Safely remove key if it exists
    if key in d:
        del d[key]
        return True
    else:
        return False

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

    print("Enter key to remove:")
    key_to_remove = input().strip()

    # Process
    removed = remove_key(d, key_to_remove)

    # Output
    if removed:
        print("Updated Dictionary after removal:")
        print(d)
    else:
        print(f"Key '{key_to_remove}' not found in dictionary.")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python remove_key.py
Enter dictionary (key:value pairs separated by space):
a:1 b:2 c:3
Enter key to remove:
b
Updated Dictionary after removal:
{'a': 1, 'c': 3}
