# second_largest.py

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements

    # Initialize first and second largest
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            # Update both largest and second largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update only second largest
            second_largest = num

    return second_largest if second_largest != float('-inf') else None


# Example usage
if __name__ == "__main__":
    data = [12, 35, 1, 10, 34, 1]
    result = find_second_largest(data)
    if result is not None:
        print("Second largest element:", result)
    else:
        print("No second largest element found.")
