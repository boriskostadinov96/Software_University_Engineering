def find_string(first_letter, second_letter):
    result = ''

    for current_char in range(ord(first_letter) + 1, ord(second_letter), + 1):
        result += chr(current_char) + ' '

    print(result)


first_char = input()
second_char = input()

find_string(first_char, second_char)

# solution 2
#
# def all_the_characters(first_char: str, second_char: str) -> list:
#     characters = []
#     for current_character_as_digit in range(ord(first_char) + 1, ord(second_char)):
#         characters.append(chr(current_character_as_digit))
#     return characters
#
#
# first_character = input()
# second_character = input()
# final_result = all_the_characters(first_character, second_character)
# print(" ".join(final_result))
