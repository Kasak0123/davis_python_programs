# Inverted Left Triangle Pattern

def inverted_left_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    inverted_left_triangle(rows)