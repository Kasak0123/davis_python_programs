import numpy as np

# Create a 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, size=(5, 5))

# Find minimum and maximum values
min_val = matrix.min()
max_val = matrix.max()

print("Matrix:")
print(matrix)
print("\nMin =", min_val)
print("Max =", max_val)
