def smart_login_system():
    # Predefined credentials (for demo purposes)
    valid_username = "admin"
    valid_password = "password123"

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Username validation
        if username != valid_username:
            print("Invalid username.")
            attempts += 1
        # Password validation
        elif password != valid_password:
            print("Invalid password.")
            attempts += 1
        else:
            print("Login Successful!")
            return

        print(f"Attempts left: {max_attempts - attempts}")

    print("Account Locked due to 3 failed attempts.")


# Example usage:
smart_login_system()