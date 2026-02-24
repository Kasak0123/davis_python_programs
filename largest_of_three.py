# Read input from standard input
a, b, c = map(int, input().split())

# Check which is largest
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python largest_of_three.py
1 9 5
9
