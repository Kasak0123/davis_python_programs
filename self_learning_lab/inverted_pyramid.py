# Inverted Pyramid Pattern

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        # Leading spaces to center the pyramid
        print(" " * (n - i), end="")
        # Stars for the current row
        print("* " * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    inverted_pyramid(rows)