def username_field_validator(username):
    if username and len(username) >= 3:
        return True
    return False