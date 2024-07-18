lessons = input().split(', ')
command = input().split(':')
schedule = lessons

while command[0] != "course start":

    if command[0] == 'Add':
        if command[1] not in schedule:
            schedule.append(command[1])

    elif command[0] == 'Insert':
        if command[1] not in schedule:
            schedule.insert(int(command[2]), command[1])

    elif command[0] == 'Remove':
        if command[1] in schedule:
            schedule.remove(command[1])
            exercise = command[1] + "-Exercise"

            if exercise in schedule:
                schedule.remove(exercise)

    elif command[0] == 'Swap':
        lesson1 = command[1]
        lesson2 = command[2]

        if lesson1 in schedule and lesson2 in schedule:
            index1 = schedule.index(lesson1)
            index2 = schedule.index(lesson2)
            schedule[index1], schedule[index2] = schedule[index2], schedule[index1]

            exercise1 = lesson1 + "-Exercise"
            exercise2 = lesson2 + "-Exercise"

            if exercise1 in schedule:
                exercise1_index = schedule.index(exercise1)
                schedule.pop(exercise1_index)
                schedule.insert(index2 + 1, exercise1)

            if exercise2 in schedule:
                exercise2_index = schedule.index(exercise2)
                schedule.pop(exercise2_index)
                schedule.insert(index1 + 1, exercise2)

    elif command[0] == "Exercise":
        lesson = command[1]
        exercise = lesson + "-Exercise"

        if lesson in schedule:
            lesson_index = schedule.index(lesson)

            if exercise not in schedule:
                schedule.insert(lesson_index + 1, exercise)
        else:
            schedule.append(lesson)
            schedule.append(exercise)

    command = input().split(':')

for index, lesson in enumerate(schedule, start=1):
    print(f'{index}.{lesson}')
