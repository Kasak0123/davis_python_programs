# Read input from standard input
year = int(input())

# Check leap year conditions
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python leap_year.py
2024
Leap Year
