# Continuous Square Pattern

def continuous_square(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(num, end=" ")
            num += 1
        print()

if __name__ == "__main__":
    rows = int(input("Enter size of square: "))
    continuous_square(rows)