def salary_processing_system(salaries, min_wage=30000):
    # Step 1: Remove salaries below minimum wage
    valid_salaries = [s for s in salaries if s >= min_wage]
    
    # Step 2: Add 5% bonus for salaries > 50,000
    updated_salaries = []
    for s in valid_salaries:
        if s > 50000:
            s *= 1.05
        updated_salaries.append(round(s, 2))
    
    # Step 3: Sort in descending order
    sorted_salaries = sorted(updated_salaries, reverse=True)
    
    # Step 4: Display top 3 highest salaries
    top_3 = sorted_salaries[:3]
    
    # Step 5: Print results
    print("Valid Salaries:", valid_salaries)
    print("Updated Salaries (with bonus):", updated_salaries)
    print("Sorted Salaries (Descending):", sorted_salaries)
    print("Top 3 Highest Salaries:", top_3)


# Example usage
salaries_list = [30000, 45000, 52000, 70000, 25000, 80000]
salary_processing_system(salaries_list)