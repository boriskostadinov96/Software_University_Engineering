command = input()
max_number = int(command)

while command != "Stop":
    number = int(command)

    if number > max_number:
        max_number = number

    command = input()

print(max_number)


# solution 2
# from math import inf
#
# command = input()
# max_number = -inf
#
# while command != "Stop":
#     current_number = int(command)
#
#     if current_number > max_number:
#         max_number = current_number
#
#     command = input()
#
# print(max_number)