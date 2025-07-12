import re

def is_password_safe(password: str) -> str:
    check_match = re.match(r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,})", password)
    if not check_match:
        raise ValueError("Password must be at least 8 characters long and contain at least one digit, one lowercase letter, one uppercase letter, and one special character.")

    return password

def is_email_valid(email: str) -> bool:
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)