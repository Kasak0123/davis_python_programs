# Read input from standard input
username = input().strip()
password = input().strip()

# Function to validate username
def validate_username(u):
    return u.isalnum() and len(u) >= 5

# Function to validate password
def validate_password(p):
    if len(p) < 8:
        return False
    has_upper = any(ch.isupper() for ch in p)
    has_lower = any(ch.islower() for ch in p)
    has_digit = any(ch.isdigit() for ch in p)
    has_special = any(not ch.isalnum() for ch in p)
    return has_upper and has_lower and has_digit and has_special

# Check both
if validate_username(username) and validate_password(password):
    print("Valid")
else:
    print("Invalid")

## output
PS C:\Users\hp\OneDrive\Desktop\python_coding_problems> python validate_user.py
Kasak123
Pass@123
Valid
