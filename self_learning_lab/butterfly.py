# Butterfly Pattern

def butterfly(n):
    # Upper half
    for i in range(1, n + 1):
        # Left wing
        print("*" * i, end="")
        # Spaces in the middle
        print(" " * (2 * (n - i)), end="")
        # Right wing
        print("*" * i)
    
    # Lower half
    for i in range(n, 0, -1):
        # Left wing
        print("*" * i, end="")
        # Spaces in the middle
        print(" " * (2 * (n - i)), end="")
        # Right wing
        print("*" * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    butterfly(rows)