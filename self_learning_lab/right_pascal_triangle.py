# Right Pascal Triangle Pattern

def right_pascal_triangle(n):
    # Upper half (increasing triangle)
    for i in range(1, n + 1):
        print("* " * i)
    
    # Lower half (decreasing triangle)
    for i in range(n - 1, 0, -1):
        print("* " * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    right_pascal_triangle(rows)