from .models import User
import re


def username_field_validator(username):
    if len(username.strip()) >= 3:
        return True
    return False

def email_field_validator(email):
    email_regex_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(email_regex_pattern, email):
        exists_email = User.objects.filter(email=email)
        if not exists_email:
            return True
    return False

def password_field_validator(pswd):
    if len(pswd.strip()) >= 6:
        return True
    return False
