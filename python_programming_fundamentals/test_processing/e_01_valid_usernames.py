def check_length_is_valid(user):
    if 3 <= len(user) <= 16:
        return True
    return False


def contains_is_valid(user):
    for char in user:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False

    return True


def no_redundant_check(user):
    if " " in user:
        return False
    return True


def username_is_valid(user):
    if check_length_is_valid(user) and contains_is_valid(user) and no_redundant_check(user):
        return True
    return False


usernames = input().split(', ')

for username in usernames:
    if username_is_valid(username):
        print(username)