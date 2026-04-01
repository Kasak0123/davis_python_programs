# normalize_array.py

import numpy as np

def normalize_array(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    # Apply normalization formula
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized


# Example usage
if __name__ == "__main__":
    data = np.array([10, 20, 30, 40, 50])
    result = normalize_array(data)
    print("Normalized array:", result)
