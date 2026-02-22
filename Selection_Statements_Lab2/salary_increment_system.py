def calculate_increment(rating, experience, attendance):
    increment = 0

    # Performance rating factor
    if rating == 5:
        increment += 20   # Outstanding
    elif rating == 4:
        increment += 15   # Very Good
    elif rating == 3:
        increment += 10   # Good
    elif rating == 2:
        increment += 5    # Average
    else:
        increment += 0    # Poor

    # Experience factor
    if experience >= 10:
        increment += 10
    elif experience >= 5:
        increment += 5
    else:
        increment += 2

    # Attendance factor
    if attendance >= 95:
        increment += 5
    elif attendance >= 85:
        increment += 3
    else:
        increment += 0

    return increment


# Example usage:
rating = int(input("Enter performance rating (1–5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment_percentage = calculate_increment(rating, experience, attendance)
print(f"Increment Percentage: {increment_percentage}%")