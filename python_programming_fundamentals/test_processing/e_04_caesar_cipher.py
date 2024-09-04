cipher = input()
encrypted_message = ""

for el in cipher:
    ord_message = ord(el) + 3
    chr_message = chr(ord_message)

    encrypted_message += chr_message

print(encrypted_message)


# solution 2
# message = input()
# encrypted_message = ""
#
# for character in message:
#     encrypted_character = chr(ord(character) + 3)
#     encrypted_message += encrypted_character
#
# print(encrypted_message)