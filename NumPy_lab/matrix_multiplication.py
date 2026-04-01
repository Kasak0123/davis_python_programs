import numpy as np

# Define Matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Define Matrix B
B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Perform matrix multiplication
result = np.dot(A, B)

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of A x B:")
print(result)
