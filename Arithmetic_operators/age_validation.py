# Program for Age Validation

age = int(input("Enter your age: "))

# Validation
if age < 0:
    print("Invalid age: Age cannot be negative.")
elif age > 150:
    print("Invalid age: Age seems unrealistic.")
else:
    print("Valid age entered.")

    # Optional categorization
    if age < 18:
        print("You are a minor.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")