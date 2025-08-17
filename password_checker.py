import re

def check_password_strength(password: str) -> str:
    """
    Check the strength of a given password based on:
    - Length (>= 8 characters)
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special characters
    """
    strength_points = 0

    # Check length
    if len(password) >= 8:
        strength_points += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength_points += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength_points += 1

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength_points += 1

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1

    # Strength categories
    if strength_points == 5:
        return "Strong Password 💪"
    elif 3 <= strength_points < 5:
        return "Moderate Password ⚠️"
    else:
        return "Weak Password ❌"


if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    user_password = input("Enter a password to check: ")
    result = check_password_strength(user_password)
    print(f"Result: {result}")
