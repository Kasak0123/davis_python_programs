# File: check_key.py
# Problem: Check whether key exists in dictionary

def check_key_exists(d, key):
    return key in d

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

    print("Enter key to check:")
    key_to_check = input().strip()

    # Process
    exists = check_key_exists(d, key_to_check)

    # Output
    if exists:
        print(f"Key '{key_to_check}' exists in dictionary.")
    else:
        print(f"Key '{key_to_check}' does not exist in dictionary.")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python check_key.py
Enter dictionary (key:value pairs separated by space):
a:1 b:2 c:3
Enter key to check:
b
Key 'b' exists in dictionary.
