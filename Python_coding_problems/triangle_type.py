# Function to determine triangle type
def triangle_type(a, b, c):
    # Check if valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a Triangle"
    
    # Equilateral: all sides equal
    if a == b == c:
        return "Equilateral"
    
    # Isosceles: any two sides equal
    elif a == b or b == c or a == c:
        return "Isosceles"
    
    # Scalene: all sides different
    else:
        return "Scalene"

# Main program
if __name__ == "__main__":
    # Read input from standard input
    sides = list(map(int, input("Enter three sides separated by space: ").split()))
    
    if len(sides) != 3:
        print("Invalid input. Please enter exactly three sides.")
    else:
        a, b, c = sides
        print(triangle_type(a, b, c))

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python triangle_type.py
Enter three sides separated by space: 3 3 3
Equilateral
