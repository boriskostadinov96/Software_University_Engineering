MAX_SIZE = 4

people = int(input())
wagons = [int(x) for x in input().split()]

for i in range(len(wagons)):
    free_spaces = MAX_SIZE - wagons[i]

    if people >= free_spaces:
        wagons[i] += free_spaces

    else:
        wagons[i] += people

    people -= free_spaces

    if people <= 0 and (i != len(wagons) - 1 or wagons[i] < MAX_SIZE):
        print('The lift has empty spots!')
        break

else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*wagons)