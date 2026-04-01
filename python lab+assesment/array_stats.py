# array_stats.py

import numpy as np

def calculate_stats(arr):
    mean_val = np.mean(arr)
    median_val = np.median(arr)
    std_dev = np.std(arr)
    return mean_val, median_val, std_dev


# Example usage
if __name__ == "__main__":
    data = np.array([10, 20, 30, 40, 50])
    mean, median, std_dev = calculate_stats(data)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)
