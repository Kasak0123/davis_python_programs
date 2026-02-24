# Function to return unique elements from a list
def get_unique_elements(lst):
    return list(set(lst))

# Read input from standard input
numbers = list(map(int, input().split()))

# Call the function and print result
unique_list = get_unique_elements(numbers)
print(unique_list)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python unique_elements.py
1 2 2 3 4 4 5
[1, 2, 3, 4, 5]
