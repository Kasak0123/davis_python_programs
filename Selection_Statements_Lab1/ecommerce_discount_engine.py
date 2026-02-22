def calculate_discount(cart_value, membership, festival=False):
    # Base discounts based on cart value
    if cart_value >= 10000:
        cart_discount = 0.10   # 10%
    elif cart_value >= 5000:
        cart_discount = 0.05   # 5%
    else:
        cart_discount = 0.02   # 2%

    # Membership discounts
    membership_discounts = {
        "Silver": 0.05,   # 5%
        "Gold": 0.10,     # 10%
        "Platinum": 0.15  # 15%
    }
    membership_discount = membership_discounts.get(membership, 0)

    # Festival discount
    festival_discount = 0.07 if festival else 0

    # Apply the highest discount
    highest_discount = max(cart_discount, membership_discount, festival_discount)

    final_amount = cart_value * (1 - highest_discount)
    return highest_discount, final_amount


# Example usage:
cart_value = float(input("Enter cart value (₹): "))
membership = input("Enter membership type (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ").lower() == "yes"

discount, payable = calculate_discount(cart_value, membership, festival)

print(f"Highest discount applied: {discount*100:.0f}%")
print(f"Final payable amount: ₹{payable:.2f}")