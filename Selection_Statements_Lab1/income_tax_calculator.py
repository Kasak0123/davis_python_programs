def calculate_tax(income, age):
    # Adjust exemption limit for senior citizens
    if age >= 60:
        exemption_limit = 300000
    else:
        exemption_limit = 250000

    tax = 0

    if income <= exemption_limit:
        tax = 0
    elif income <= 500000:
        tax = (income - exemption_limit) * 0.05
    elif income <= 1000000:
        tax = (500000 - exemption_limit) * 0.05 + (income - 500000) * 0.20
    else:
        tax = (500000 - exemption_limit) * 0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30

    return tax


# Example usage:
income = float(input("Enter your annual income (₹): "))
age = int(input("Enter your age: "))

tax = calculate_tax(income, age)
print(f"Your calculated tax is: ₹{tax:.2f}")