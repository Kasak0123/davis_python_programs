import numpy as np

# Create array from 1 to 10
arr = np.arange(1, 11)

# Replace even numbers with 0
arr[arr % 2 == 0] = 0

print(arr)
