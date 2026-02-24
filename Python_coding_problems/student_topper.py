# File: student_topper.py
# Problem: Create student marks dictionary and find topper

# Input Format:
# First line: number of students
# Next lines: student name and marks separated by space
# Example:
# 3
# Alice 85
# Bob 92
# Charlie 78

n = int(input())  # number of students
marks_dict = {}

# Read student names and marks
for _ in range(n):
    name, marks = input().split()
    marks_dict[name] = int(marks)

# Find topper (student with maximum marks)
topper = max(marks_dict, key=marks_dict.get)

# Output Format: Print topper's name and marks
print("Topper:", topper, marks_dict[topper])

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python student_topper.py
3
Alice 85
Bob 92
Charlie 78
Topper: Bob 92
