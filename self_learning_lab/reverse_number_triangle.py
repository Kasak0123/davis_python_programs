# Reverse Alphabet Triangle Pattern

def reverse_alphabet_triangle(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print(chr(65 + j), end=" ")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    reverse_alphabet_triangle(rows)