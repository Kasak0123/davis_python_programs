# Hollow Diamond Pattern

def hollow_diamond(n):
    # Upper half
    for i in range(1, n + 1):
        # Leading spaces
        print(" " * (n - i), end="")
        # First star
        print("*", end="")
        # Hollow space inside (only if row > 1)
        if i > 1:
            print(" " * (2 * i - 3), end="")
            # Second star
            print("*", end="")
        print()
    
    # Lower half
    for i in range(n - 1, 0, -1):
        # Leading spaces
        print(" " * (n - i), end="")
        # First star
        print("*", end="")
        # Hollow space inside (only if row > 1)
        if i > 1:
            print(" " * (2 * i - 3), end="")
            # Second star
            print("*", end="")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    hollow_diamond(rows)