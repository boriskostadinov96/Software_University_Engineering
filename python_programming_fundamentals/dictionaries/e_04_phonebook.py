command = input()
phonebook = {}

while '-' in command:
    person, phone_number = command.split('-')
    phonebook[person] = phone_number

    command = input()

count = int(command)
for _ in range(count):
    current_person = input()

    if current_person in phonebook:
        print(f"{current_person} -> {phonebook[current_person]}")
    else:
        print(f"Contact {current_person} does not exist.")
