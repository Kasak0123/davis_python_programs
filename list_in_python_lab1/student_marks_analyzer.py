def student_marks_analyzer(marks):
    # Step 1: Remove invalid marks
    valid_marks = [m for m in marks if 0 <= m <= 100]
    
    if not valid_marks:
        return "No valid marks available."
    
    # Step 2: Calculate average
    average = sum(valid_marks) / len(valid_marks)
    
    # Step 3: Find topper(s)
    max_mark = max(valid_marks)
    toppers = [i+1 for i, m in enumerate(valid_marks) if m == max_mark]  # student indices
    
    # Step 4: Assign grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"
    
    # Step 5: Display results
    print("Valid Marks:", valid_marks)
    print("Average Marks:", round(average, 2))
    print("Topper(s): Student(s)", toppers, "with marks:", max_mark)
    print("Class Grade:", grade)


# Example usage
marks_list = [95, 82, -5, 101, 76, 89, 100]
student_marks_analyzer(marks_list)