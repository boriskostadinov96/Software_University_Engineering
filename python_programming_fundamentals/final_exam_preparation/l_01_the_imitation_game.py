decrypted_message = input()
command = input()

while command != "Decode":
    operations = command.split('|')

    if operations[0] == 'Move':
        letters = int(operations[1])

        first_part = decrypted_message[:letters]
        second_part = decrypted_message[letters:]
        decrypted_message = second_part + first_part

    elif operations[0] == 'Insert':
        index = int(operations[1])
        value = operations[2]
        decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]

    elif operations[0] == 'ChangeAll':
        substring = operations[1]
        replace_str = operations[2]

        decrypted_message = decrypted_message.replace(substring, replace_str)

    command = input()

print(f"The decrypted message is: {decrypted_message}")
