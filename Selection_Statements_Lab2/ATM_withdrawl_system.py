def atm_withdrawal(account_balance, withdrawal_amount, atm_cash, daily_limit=50000):
    # Condition 1: Account balance must be sufficient
    if withdrawal_amount > account_balance:
        return "Transaction Failed: Insufficient account balance."

    # Condition 2: Daily withdrawal limit
    if withdrawal_amount > daily_limit:
        return f"Transaction Failed: Withdrawal amount exceeds daily limit of ₹{daily_limit}."

    # Condition 3: ATM cash availability
    if withdrawal_amount > atm_cash:
        return "Transaction Failed: ATM has insufficient cash."

    # If all conditions pass
    account_balance -= withdrawal_amount
    atm_cash -= withdrawal_amount
    return f"Transaction Successful! Amount withdrawn: ₹{withdrawal_amount}. Remaining balance: ₹{account_balance}."


# Example usage:
account_balance = float(input("Enter account balance (₹): "))
withdrawal_amount = float(input("Enter withdrawal amount (₹): "))
atm_cash = float(input("Enter ATM available cash (₹): "))

result = atm_withdrawal(account_balance, withdrawal_amount, atm_cash)
print(result)