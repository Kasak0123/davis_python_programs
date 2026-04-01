# replace_odds.py

import numpy as np

def replace_odds(arr):
    # Use boolean indexing to replace odd numbers
    arr[arr % 2 != 0] = -1
    return arr


# Example usage
if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5, 6, 7])
    result = replace_odds(data)
    print("Modified array:", result)
