def inventory_management(stock_list):
    # Step 1: Remove items with 0 stock
    valid_stock = [s for s in stock_list if s > 0]
    
    # Step 2: Add restock (50 units) to items below 10
    updated_stock = []
    for s in valid_stock:
        if s < 10:
            s += 50
        updated_stock.append(s)
    
    # Step 3: Find total inventory count
    total_inventory = sum(updated_stock)
    
    # Step 4: Display results
    print("Original Stock:", stock_list)
    print("After Removing Zero Stock:", valid_stock)
    print("After Restocking (<10 +50):", updated_stock)
    print("Total Inventory Count:", total_inventory)


# Example usage
stock_quantities = [0, 5, 12, 8, 50, 0, 3]
inventory_management(stock_quantities)