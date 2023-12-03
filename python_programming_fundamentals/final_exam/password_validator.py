password = input()

while True:
    commands = input()
    if commands == "Complete":
        break
    asd = commands.split(" ")
    command = asd[0]
    if command == 'Insert':
        char = asd[2]
        n = int(asd[1])
        if n < len(password):
            password = password[:n] + char + password[n:]
            print(password)
        else:
            pass
    if command == 'Make':
        command = asd[1]
        n = int(asd[2])
        if command == 'Upper':
            password = password[:n] + password[n].upper() + password[n + 1:]
            print(password)
        elif command == 'Lower':
            password = password[:n] + password[n].lower() + password[n + 1:]
            print(password)
    elif command == 'Replace':
        char = asd[1]
        n = int(asd[2])
        if char not in password:
            pass
        else:
            sum = int(ord(char) + n)
            char1 = chr(sum)
            password = password.replace(char, char1)
            print(password)

    elif command == 'Validation':
        if len(password) < 8:
            print('Password must be at least 8 characters long')
        elif password.isalnum() == False and '_!"' not in password:
            print('Password must consist only of letters, digits and _!"')
        elif not any(x.isupper() for x in password):
            print('Password must consist at least one uppercase letter!')
        elif not any(x.islower() for x in password):
            print('Password must consist at least one lowercase letter!')
        elif not any(x.isdigit() for x in password):
            print('Password must consist at least one digit!')