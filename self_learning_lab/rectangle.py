# Rectangle Pattern

def rectangle_pattern(rows, cols):
    for i in range(rows):
        print("* " * cols)

if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    rectangle_pattern(r, c)