def check_is_password_valid(some_password):
    digits_counter = 0
    is_valid = True

    if not 6 <= len(some_password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    for character in some_password:
        if character.isdigit():
            digits_counter += 1

    if digits_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


password = input()
check_is_password_valid(password)


# solution 2
#
# def password_validator(some_password: str) -> list:
#     list_of_errors = []
#     digits_counter = 0
#
#     if len(some_password) < 6 or len(some_password) > 10:
#         list_of_errors.append("Password must be between 6 and 10 characters")
#
#     if not some_password.isalnum():
#         list_of_errors.append("Password must consist only of letters and digits")
#
#     for character in some_password:
#         if character.isdigit():
#             digits_counter += 1
#
#     if digits_counter < 2:
#         list_of_errors.append("Password must have at least 2 digits")
#
#     return list_of_errors
#
#
# password = input()
# errors_in_password = password_validator(password)

if not errors_in_password:
    print("Password is valid")

else:
    print("\n".join(errors_in_password))