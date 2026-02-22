# Program to calculate Simple Interest

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (per year): "))
time = float(input("Enter the time (in years): "))

# Formula for Simple Interest
simple_interest = (principal * rate * time) / 100

# Output
print("The Simple Interest is:", simple_interest)