lines = int(input())

for _ in range(lines):
    text = input()
    name_start_index = text.find('@') + 1
    name_end_index = text.find('|')
    name = text[name_start_index:name_end_index]

    age_start_index = text.find('#') + 1
    age_end_index = text.find('*')
    age = text[age_start_index:age_end_index]

    print(f"{name} is {age} years old.")


# solution 2
# number_of_lines = int(input())
#
# for index in range(number_of_lines):
#     line = input()
#     name = ""
#     age = ""
#     name_found = False
#     age_found = False
#
#     for char in line:
#         if char == "@":
#             name_found = True
#             continue
#
#         if char == "|":
#             name_found = False
#
#         if name_found:
#             name += char
#
#         if char == "#":
#             age_found = True
#             continue
#
#         if char == "*":
#             age_found = False
#
#         if age_found:
#             age += char
#
#     print(f"{name} is {age} years old.")