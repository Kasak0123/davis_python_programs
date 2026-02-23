# Inverted Right-Angle Triangle Pattern

def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        # Leading spaces to push stars to the right
        print(" " * (n - i), end="")
        # Stars for the current row
        print("* " * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    inverted_right_triangle(rows)