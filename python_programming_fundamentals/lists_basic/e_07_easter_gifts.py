gifts = input().split()
command = input().split()

while command != "No Money":
    action = command[0]
    gift_name = command[1]

    if action == "No" and gift_name == "Money":
        break

    if action == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == gift_name:
                gifts[i] = "None"

    elif action == "Required":
        gift_name = command[1]
        index = int(command[2])

        if 0 <= index < len(gifts):
            gifts[index] = gift_name

    elif action == "JustInCase":
        gifts[-1] = gift_name

    command = input().split()

gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(gifts))

# solution 2
# gifts = input()
# list_of_gifts = gifts.split(' ')
# command = input()
#
# while command != 'No Money':
#
#     if 'OutOfStock' in command:
#         action, value = command.split(' ')
#
#         for i in range(len(list_of_gifts)):
#             if value == list_of_gifts[i]:
#                 list_of_gifts[i] = 'None'
#
#     elif "Required" in command:
#         action, value, index = command.split(' ')
#         # value = command.split(' ')[1]
#         # index = command.split(' ')[2]
#         index = int(index)
#
#         for i in range(len(list_of_gifts)):
#             if index == i:
#                 list_of_gifts[i] = value
#
#     elif "JustInCase" in command:
#         action,value = command.split(' ')
#         # value = command.split(" ")[1]
#         list_of_gifts.pop()
#         list_of_gifts.append(value)
#
#     command = input()
#
# list_of_gifts = [gift for gift in list_of_gifts if gift != 'None']
# print(" ".join(list_of_gifts))

