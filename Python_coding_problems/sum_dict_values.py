# File: sum_dict_values.py
# Problem: Find sum of all dictionary values

def sum_dict_values(d):
    return sum(d.values())

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
            print(f"Skipping non-numeric value for key '{key}'")
    
    # Process
    total = sum_dict_values(d)

    # Output
    print("Sum of all dictionary values:")
    print(total)

if __name__ == "__main__":
    main()

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python sum_dict_values.py
Enter dictionary (key:value pairs separated by space):
a:10 b:20 c:30
Sum of all dictionary values:
60
