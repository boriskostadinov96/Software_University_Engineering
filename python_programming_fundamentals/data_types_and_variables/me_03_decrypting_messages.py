key = int(input())
lines = int(input())
decrypted_message = ""

for _ in range(lines):
    letter = input()

    ord_message = key + ord(letter)
    chr_message = chr(ord_message)
    decrypted_message += chr_message

print(decrypted_message)

# solution 2
# key = int(input())
# number_of_lines = int(input())
# end_result = ""
#
# for index in range(number_of_lines):
#     current_character = input()
#     ascii_letter = ord(current_character)
#     ascii_letter += key
#     end_result = chr(ascii_letter)
#     print(end_result, end="")
