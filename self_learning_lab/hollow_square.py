# Hollow Square Pattern

def hollow_square(n):
    for i in range(1, n + 1):
        # First and last row should be filled
        if i == 1 or i == n:
            print("* " * n)
        else:
            # First star
            print("*", end=" ")
            # Hollow space inside
            print("  " * (n - 2), end="")
            # Last star
            print("*")
            
if __name__ == "__main__":
    size = int(input("Enter size of square: "))
    hollow_square(size)