# armstrong_check.py

def is_armstrong(n):
    # Convert number to string to count digits
    num_str = str(n)
    num_digits = len(num_str)

    # Calculate sum of digits raised to the power of num_digits
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits

    # Check Armstrong condition
    return total == n


# Example usage
if __name__ == "__main__":
    number = 153
    result = is_armstrong(number)
    print(f"{number} is Armstrong? {result}")
