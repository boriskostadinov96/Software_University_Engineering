wagons = int(input())
command = input().split()
train = [0] * wagons

while command[0] != "End":

    if command[0] == 'add':
        train[-1] += int(command[1])

    elif command[0] == 'insert':
        index = int(command[1])
        train[index] += int(command[2])

    elif command[0] == 'leave':
        index = int(command[1])
        train[index] -= int(command[2])

    command = input().split()

print(train)

# solution 2
# number_of_wagons = [0 for x in range(int(input()))]
# command = input()
#
# while command != 'End':
#
#     if "add" in command:
#         action, people = command.split()
#         people = int(people)
#         number_of_wagons[len(number_of_wagons) - 1] += people
#
#     elif "insert" in command:
#         action, index, people = command.split()
#         index = int(index)
#         people = int(people)
#         number_of_wagons[index] += people
#
#     elif "leave" in command:
#         action, index, people = command.split()
#         index = int(index)
#         people = int(people)
#         number_of_wagons[index] -= people
#
#     command = input()
#
# print(number_of_wagons)