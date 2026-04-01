# matrix_multiply.py

import numpy as np

def multiply_matrices(A, B):
    # Perform matrix multiplication using np.dot or @ operator
    return np.dot(A, B)


# Example usage
if __name__ == "__main__":
    # Define two matrices
    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])

    result = multiply_matrices(A, B)
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("Result of multiplication:\n", result)
