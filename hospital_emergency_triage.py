def triage_system(age, heart_rate_abnormal, severe_injury):
    # Step 1: Check for critical condition
    if heart_rate_abnormal or severe_injury:
        return "Critical"

    # Step 2: Default to Moderate if not critical
    category = "Moderate"

    # Step 3: Upgrade priority if age > 65 and condition is moderate
    if age > 65 and category == "Moderate":
        return "Upgraded to Critical (due to age > 65)"

    # Step 4: If none of the above, Normal
    return "Normal"


# Example usage:
age = int(input("Enter patient's age: "))
heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ").lower() == "yes"
severe_injury = input("Does patient have severe injury? (yes/no): ").lower() == "yes"

category = triage_system(age, heart_rate_abnormal, severe_injury)
print(f"Patient triage category: {category}")