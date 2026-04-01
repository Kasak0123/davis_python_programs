import numpy as np

# Create array from 1 to 15
arr = np.arange(1, 16)

# Find numbers greater than 10
greater_than_10 = arr[arr > 10]

print("Array:", arr)
print("Numbers greater than 10:", greater_than_10)
