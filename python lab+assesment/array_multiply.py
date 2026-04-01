# array_multiply.py

import numpy as np

def elementwise_multiply(arr1, arr2):
    # Perform element-wise multiplication
    return arr1 * arr2


# Example usage
if __name__ == "__main__":
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    result = elementwise_multiply(a, b)
    print("Resultant array:", result)
