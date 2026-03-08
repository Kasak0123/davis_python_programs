# File: max_value_key.py
# Problem: Find key with maximum value

def find_max_value_key(d):
    # Find the key with the maximum value
    max_key = max(d, key=d.get)
    return max_key, d[max_key]

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
    key, value = find_max_value_key(d)

    # Output
    print("Key with maximum value:")
    print(f"{key}: {value}")

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python max_value_key.py
Enter dictionary (key:value pairs separated by space):
a:10 b:25 c:15
Key with maximum value:
b: 25
