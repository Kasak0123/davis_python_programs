# 0-1 Triangle Pattern

def zero_one_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # Print 1 if sum of row and column is even, else 0
            print((i + j) % 2, end=" ")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    zero_one_triangle(rows)