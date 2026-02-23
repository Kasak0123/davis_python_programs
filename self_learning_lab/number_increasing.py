# Number Increasing Triangle Pattern

def number_increasing(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    number_increasing(rows)