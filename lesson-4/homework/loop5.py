def check_password(password):
    # Check password length
    if len(password) < 8:
        print("Password is too short.")
    # Ensure at least one uppercase letter exists
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")
