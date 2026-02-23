def ecommerce_cart_system(cart_prices):
    # Step 1: Remove duplicates
    unique_prices = list(set(cart_prices))
    
    # Step 2: Calculate total
    total = sum(unique_prices)
    
    # Step 3: Apply discount if total > 5000
    if total > 5000:
        total *= 0.90   # 10% discount
    
    # Step 4: Add GST 18%
    final_amount = total * 1.18
    
    # Step 5: Display results
    print("Unique Cart Prices:", unique_prices)
    print("Total after discount (if any): ₹", round(total, 2))
    print("Final Payable Amount (with GST): ₹", round(final_amount, 2))


# Example usage
cart = [1200, 2500, 2500, 1800, 3000]
ecommerce_cart_system(cart)