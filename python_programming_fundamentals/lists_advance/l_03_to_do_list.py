notes = input()
to_do_list = [0] * 10

while notes != "End":
    importance, task = notes.split('-')
    importance = int(importance)
    index = importance - 1
    to_do_list[index] = task

    notes = input()

print([t for t in to_do_list if t != 0])
