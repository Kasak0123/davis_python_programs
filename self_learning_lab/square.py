# Square Pattern

def square_pattern(n):
    for i in range(n):
        print("* " * n)

if __name__ == "__main__":
    size = int(input("Enter size of square: "))
    square_pattern(size)