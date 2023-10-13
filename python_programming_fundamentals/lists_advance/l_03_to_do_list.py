command = input()
notes = [0] * 10

while command != "End":
    importance, task = command.split('-')
    importance = int(importance)
    index = importance - 1
    notes[index] = task
    command = input()

print([task for task in notes if task != 0])