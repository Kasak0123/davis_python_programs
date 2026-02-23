def temperature_monitoring_system(temperatures):
    # Step 1: Find hottest and coldest day
    hottest = max(temperatures)
    coldest = min(temperatures)
    
    # Step 2: Replace temperatures above 45°C with "Heat Alert"
    flagged_temps = ["Heat Alert" if t > 45 else t for t in temperatures]
    
    # Step 3: Count number of extreme days (> 40°C)
    extreme_days = sum(1 for t in temperatures if t > 40)
    
    # Step 4: Display results
    print("Original Temperatures:", temperatures)
    print("Hottest Day Temperature:", hottest)
    print("Coldest Day Temperature:", coldest)
    print("Flagged Temperatures:", flagged_temps)
    print("Number of Extreme Days (>40°C):", extreme_days)


# Example usage
daily_temps = [32, 38, 41, 29, 46, 35, 44, 20]
temperature_monitoring_system(daily_temps)