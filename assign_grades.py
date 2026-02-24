# Read input from standard input
marks = int(input())

# Assign grades based on marks
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Grade F")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python grades_marks.py
98
Grade A
