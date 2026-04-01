# extract_diagonal.py

import numpy as np

def extract_diagonal(matrix):
    return np.diagonal(matrix)   # NumPy provides a direct method


# Example usage
if __name__ == "__main__":
    data = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
    result = extract_diagonal(data)
    print("Diagonal elements:", result)
