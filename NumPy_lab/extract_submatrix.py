import numpy as np

# Create array from 1 to 25
arr = np.arange(1, 26)

# Reshape into 5x5 matrix
matrix = arr.reshape(5, 5)

# Extract the middle 3x3 sub-matrix
sub_matrix = matrix[1:4, 1:4]

print("Matrix:")
print(matrix)
print("\nMiddle 3x3 Sub-matrix:")
print(sub_matrix)
