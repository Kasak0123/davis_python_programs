def is_suspicious_transaction(amount, account_age_months, is_international):
    # Conditions:
    # 1. Transaction amount > ₹2,00,000
    # 2. Account age < 6 months
    # 3. Transaction is international
    
    if amount > 200000 and account_age_months < 6 and is_international:
        return True
    else:
        return False


# Example usage:
transaction_amount = 250000       # ₹2,50,000
account_age = 3                   # 3 months old
international = True              # International transaction

if is_suspicious_transaction(transaction_amount, account_age, international):
    print("Transaction flagged for manual verification.")
else:
    print("Transaction is normal.")