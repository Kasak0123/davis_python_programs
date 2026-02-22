def calculate_bill(units, senior_citizen=False):
    # Step 1: Calculate base bill based on slabs
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = (100 * 5) + (units - 100) * 7
    else:
        bill = (100 * 5) + (200 * 7) + (units - 300) * 10

    # Step 2: Apply senior citizen discount
    if senior_citizen:
        bill *= 0.90  # 10% discount

    return bill


# Example usage:
units = int(input("Enter units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ").lower() == "yes"

final_bill = calculate_bill(units, senior)
print(f"Final Electricity Bill: ₹{final_bill:.2f}")