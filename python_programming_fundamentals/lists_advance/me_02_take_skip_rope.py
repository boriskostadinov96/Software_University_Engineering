word = input()
numbers_list = []
non_numbers_list = []

for el in word:
    if el.isdigit():
        numbers_list.append(el)
    else:
        non_numbers_list.append(el)

even_list = [int(x) for i, x in enumerate(numbers_list) if i % 2 == 0]
odd_list = [int(x) for i, x in enumerate(numbers_list) if i % 2 != 0]

hidden_message = []
current_index = 0

for take, skip in zip(even_list, odd_list):
    hidden_message.extend(non_numbers_list[current_index:current_index + take])
    current_index += take + skip


if len(even_list) > len(odd_list):
    remaining_take = even_list[len(odd_list):]

    for take in remaining_take:
        hidden_message.extend(non_numbers_list[current_index:current_index + take])
        current_index += take

hidden_message_string = ''.join(hidden_message)
print(hidden_message_string)
