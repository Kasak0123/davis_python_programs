# Hollow Pyramid Pattern

def hollow_pyramid(n):
    for i in range(1, n + 1):
        # Leading spaces
        print(" " * (n - i), end="")
        
        # First star
        print("*", end="")
        
        # Hollow space inside (only if row > 1 and not the last row)
        if i > 1 and i < n:
            print(" " * (2 * i - 3), end="")
            # Second star
            print("*", end="")
        
        # Last row should be filled with stars
        if i == n:
            print("*" * (2 * i - 3), end="")
        
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    hollow_pyramid(rows)