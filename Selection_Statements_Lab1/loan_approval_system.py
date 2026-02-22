def loan_approval(credit_score, monthly_income, existing_loan):
    # Rule 1: Credit score check
    if credit_score < 600:
        return "Loan Rejected: Credit score below 600"
    
    # Rule 2: Credit score ≥ 750 → Approve directly
    if credit_score >= 750:
        return "Loan Approved"
    
    # Rule 3: For credit score between 600–749, check income and existing loan
    if monthly_income < 30000 and existing_loan > 500000:
        return "Loan Rejected: Income below ₹30,000 and existing loans exceed ₹5,00,000"
    
    return "Loan Approved"


# Example usage:
credit_score = int(input("Enter credit score: "))
monthly_income = float(input("Enter monthly income (₹): "))
existing_loan = float(input("Enter existing loan amount (₹): "))

decision = loan_approval(credit_score, monthly_income, existing_loan)
print(decision)