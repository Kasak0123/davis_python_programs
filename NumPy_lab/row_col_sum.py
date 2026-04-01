import numpy as np

# Create a 4x4 matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# Row-wise sum
row_sum = matrix.sum(axis=1)

# Column-wise sum
col_sum = matrix.sum(axis=0)

print("Matrix:")
print(matrix)
print("\nRow Sum:")
print(row_sum)
print("\nColumn Sum:")
print(col_sum)
