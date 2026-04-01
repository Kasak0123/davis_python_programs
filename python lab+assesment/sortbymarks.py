# sort_by_marks.py

def sort_by_marks(students):
    # Sort list of tuples by marks (second element)
    sorted_list = sorted(students, key=lambda x: x[1])
    return sorted_list


# Example usage
if __name__ == "__main__":
    data = [("Alice", 88), ("Bob", 95), ("Charlie", 70), ("David", 95)]
    result = sort_by_marks(data)
    print("Sorted list based on marks:", result)
