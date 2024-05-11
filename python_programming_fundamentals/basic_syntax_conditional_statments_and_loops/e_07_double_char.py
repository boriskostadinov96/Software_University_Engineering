command = input()

while command != 'End':
    current_string = str(command)

    if current_string == "SoftUni":
        command = input()
        continue

    for letter in current_string:
        print(letter * 2, end="")

    print()

    command = input()

# solution 2
# current_string = input()
#
# while current_string != "End":
#
#     if current_string != "SoftUni":
#         new_string = ""
#
#         for character in current_string:
#             new_string += character * 2
#
#         print(new_string)
#     
#     current_string = input()
