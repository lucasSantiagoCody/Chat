from core.utils import error_message_handler
from ninja.errors import HttpError
from .models import User
import re


def register_request_validator(request_data):
    check_username = username_field_validator(request_data.username)
    check_email = email_field_validator(request_data.email)
    check_password = password_field_validator(request_data.password)

    messages_error = []

    if not check_username:
        messages_error.append('Invalid username field')

    if check_email == 'already_exists':
        messages_error.append('This email already exits')
    elif check_email == False:
        messages_error.append('Invalid email field')

    if not check_password:
        messages_error.append('Invalid password field min 6 characters')

    single_msg = error_message_handler(messages_error)
    if single_msg:
        raise HttpError(status_code=400, message=single_msg)
    
    return True

def username_field_validator(username):
    if len(username.strip()) >= 3:
        return True
    return False

def email_field_validator(email):
    email_regex_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(email_regex_pattern, email):
        exists_email = User.objects.filter(email=email)
        if exists_email:
            return 'already_exists'
        else:
            return True
    return False

def password_field_validator(pswd):
    if len(pswd.strip()) >= 6:
        return True
    return False
