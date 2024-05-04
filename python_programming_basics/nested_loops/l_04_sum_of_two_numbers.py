start_num = int(input())
end_num = int(input())
magic_num = int(input())
counter = 0
is_equal = False

for first_combination in range(start_num, end_num + 1):
    for second_combination in range(start_num, end_num + 1):
        counter += 1

        if first_combination + second_combination == magic_num:
            is_equal = True
            break

    if is_equal:
        break

if is_equal:
    print(f"Combination N:{counter} ({first_combination} + {second_combination} = {magic_num})")

else:
    print(f"{counter} combinations - neither equals {magic_num}")


