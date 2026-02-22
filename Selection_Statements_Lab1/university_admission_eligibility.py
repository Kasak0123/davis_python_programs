def check_eligibility(percentage, studied_math, entrance_score):
    reasons = []

    # Condition 1: Minimum 75% in 12th grade
    if percentage < 75:
        reasons.append("12th grade percentage is below 75%")

    # Condition 2: Must have studied Mathematics
    if not studied_math:
        reasons.append("Mathematics was not studied in 12th grade")

    # Condition 3: Entrance exam score ≥ 80
    if entrance_score < 80:
        reasons.append("Entrance exam score is below 80")

    # Final decision
    if reasons:
        print("Not Eligible for Admission.")
        print("Reason(s):")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("Eligible for Admission.")


# Example usage:
percentage = float(input("Enter 12th grade percentage: "))
studied_math = input("Did you study Mathematics? (yes/no): ").lower() == "yes"
entrance_score = float(input("Enter entrance exam score: "))

check_eligibility(percentage, studied_math, entrance_score)