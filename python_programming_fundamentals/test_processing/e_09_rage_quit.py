text = input()
current_string = ""
final_result = ""
num = ""

for el in text:
    if not el.isdigit():

        if num:
            final_result += current_string.upper() * int(num)
            num = ""
            current_string = ""
        current_string += el

    else:
        num += el

if num:
    final_result += current_string.upper() * int(num)

unique_chars = set(final_result.upper())
print(f"Unique symbols used: {len(unique_chars)}")
print(final_result)

# solution 2
# text = input()
# rage_message = ""
# repetitions = ""
# current_symbol = ""
#
# for index in range(len(text)):
#     if not text[index].isdigit():
#         current_symbol += text[index].upper()
#
#     else:
#         for next_symbols in range(index, len(text)):
#             if not text[next_symbols].isdigit():
#                 break
#             repetitions += text[next_symbols]
#
#         rage_message += current_symbol * int(repetitions)
#         current_symbol = ""
#         repetitions = ""
#
# print(f"Unique symbols used: {len(set(rage_message))}")
# print(rage_message)