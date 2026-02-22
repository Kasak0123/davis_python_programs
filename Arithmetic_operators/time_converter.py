# Program for Time Converter

# Input time in hours and minutes
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

# Convert to total minutes
total_minutes = (hours * 60) + minutes

# Convert to total seconds
total_seconds = total_minutes * 60

# Output results
print("Total Minutes:", total_minutes)
print("Total Seconds:", total_seconds)