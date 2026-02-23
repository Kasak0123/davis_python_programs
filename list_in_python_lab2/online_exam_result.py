def exam_result_processor(scores):
    # Step 1: Remove lowest 2 scores
    sorted_scores = sorted(scores)
    trimmed_scores = sorted_scores[2:]  # remove first two
    
    # Step 2: Add grace marks (5) for scores between 30–35
    updated_scores = []
    for s in trimmed_scores:
        if 30 <= s <= 35:
            s += 5
        updated_scores.append(s)
    
    # Step 3: Count number of students passed (≥ 40)
    passed_count = sum(1 for s in updated_scores if s >= 40)
    
    # Step 4: Display results
    print("Original Scores:", scores)
    print("After Removing Lowest 2:", trimmed_scores)
    print("After Adding Grace Marks:", updated_scores)
    print("Number of Students Passed (≥40):", passed_count)


# Example usage
scores_list = [25, 32, 45, 60, 35, 90, 28, 40]
exam_result_processor(scores_list)