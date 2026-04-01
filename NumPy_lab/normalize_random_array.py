import numpy as np

# Generate 10 random numbers between 0 and 1
arr = np.random.rand(10)

# Normalize the array between 0 and 1
normalized_arr = (arr - arr.min()) / (arr.max() - arr.min())

print("Original Array:")
print(arr)
print("\nNormalized Array:")
print(normalized_arr)
