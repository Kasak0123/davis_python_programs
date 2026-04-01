# transpose_matrix.py

import numpy as np

def transpose_matrix(matrix):
    return matrix.T   # NumPy provides .T for transpose


# Example usage
if __name__ == "__main__":
    data = np.array([[1, 2, 3],
                     [4, 5, 6]])
    result = transpose_matrix(data)
    print("Original matrix:\n", data)
    print("Transposed matrix:\n", result)
