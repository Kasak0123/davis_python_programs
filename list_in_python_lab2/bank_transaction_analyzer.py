def bank_transaction_analyzer(transactions):
    # Step 1: Calculate total balance
    total_balance = sum(transactions)
    
    # Step 2: Find largest withdrawal
    withdrawals = [t for t in transactions if t < 0]
    largest_withdrawal = min(withdrawals) if withdrawals else None
    
    # Step 3: Count deposits greater than 10,000
    big_deposits = sum(1 for t in transactions if t > 10000)
    
    # Step 4: Display results
    print("Transactions:", transactions)
    print("Total Balance: ₹", total_balance)
    if largest_withdrawal is not None:
        print("Largest Withdrawal: ₹", largest_withdrawal)
    else:
        print("No withdrawals found.")
    print("Number of Deposits > ₹10,000:", big_deposits)


# Example usage
transactions_list = [15000, -5000, 20000, -12000, 8000, -3000]
bank_transaction_analyzer(transactions_list)