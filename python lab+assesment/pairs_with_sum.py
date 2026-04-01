# pairs_with_sum.py

def find_pairs(numbers, target):
    pairs = []
    n = len(numbers)

    # Check each pair
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs


# Example usage
if __name__ == "__main__":
    data = [2, 4, 3, 5, 7, 8, -1]
    target_value = 7
    result = find_pairs(data, target_value)
    print(f"Pairs with sum {target_value}:", result)
