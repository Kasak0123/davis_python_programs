# X Pattern

def x_pattern(n):
    for i in range(n):
        for j in range(n):
            # Print star if row and column indices match (diagonal)
            # or if they sum to n-1 (other diagonal)
            if i == j or i + j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    size = int(input("Enter size of X pattern: "))
    x_pattern(size)