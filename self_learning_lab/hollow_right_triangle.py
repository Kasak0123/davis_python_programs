# Hollow Right Triangle Pattern

def hollow_right_triangle(n):
    for i in range(1, n + 1):
        # First and last row should be filled
        if i == 1 or i == n:
            print("* " * i)
        else:
            # First star
            print("*", end=" ")
            # Hollow space inside
            print("  " * (i - 2), end="")
            # Last star
            print("*")
            
if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    hollow_right_triangle(rows)