def is_valid_string(text):
    if len(text) == 0:
        return False

    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for char in text:
        if char not in allowed_chars:
            return False  # Return False immediately if an invalid character is found
            
    return True

user_input = input("Enter a string to test: ")

if is_valid_string(user_input):
    print(f"'{user_input}' contains ONLY allowed characters (a-z, A-Z, 0-9).")
else:
    print(f"'{user_input}' contains invalid or special characters.")
