# Number Decreasing Triangle Pattern

def number_decreasing(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    number_decreasing(rows)