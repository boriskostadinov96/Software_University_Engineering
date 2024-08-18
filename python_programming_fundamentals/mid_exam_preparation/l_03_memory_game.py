numbers = input().split()
command = input()
turns = 0

while command != 'end':

    indexes = command.split()
    first_index = int(indexes[0])
    second_index = int(indexes[1])
    turns += 1

    if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(numbers) or second_index >= len(numbers):
        print("Invalid input! Adding additional elements to the board")
        middle_part = len(numbers) // 2
        new_element = f'-{turns}a'
        numbers.insert(middle_part, new_element)
        numbers.insert(middle_part, new_element)
    else:
        if numbers[first_index] == numbers[second_index]:
            element = numbers[first_index]
            print(f"Congrats! You have found matching elements - {element}!")

            if first_index > second_index:
                numbers.pop(first_index)
                numbers.pop(second_index)
            else:
                numbers.pop(second_index)
                numbers.pop(first_index)

            if len(numbers) == 0:
                print(f"You have won in {turns} turns!")
                break
        else:
            print("Try again!")

    command = input()

if len(numbers) > 0:
    print("Sorry you lose :(")
    print(' '.join(numbers))
