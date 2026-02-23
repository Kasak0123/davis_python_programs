# Alphabet Triangle Pattern

def alphabet_triangle(n):
    # ASCII value of 'A' is 65
    ascii_value = 65
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(ascii_value), end=" ")
            ascii_value += 1
            # Reset to 'A' if we go beyond 'Z'
            if ascii_value > 90:
                ascii_value = 65
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    alphabet_triangle(rows)