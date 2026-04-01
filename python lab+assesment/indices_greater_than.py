# indices_greater_than.py

import numpy as np

def find_indices(arr, value):
    # Use np.where to get indices
    indices = np.where(arr > value)[0]
    return indices


# Example usage
if __name__ == "__main__":
    data = np.array([10, 25, 30, 15, 5, 40])
    threshold = 20
    result = find_indices(data, threshold)
    print(f"Indices of elements greater than {threshold}:", result)
