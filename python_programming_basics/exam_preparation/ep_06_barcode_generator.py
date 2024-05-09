first_number = input()
second_number = input()

first_digit_first_num = first_number[0]
second_digit_first_num = first_number[1]
third_digit_first_num = first_number[2]
forth_digit_first_num = first_number[3]

first_digit_second_num = second_number[0]
second_digit_second_num = second_number[1]
third_digit_second_num = second_number[2]
forth_digit_second_num = second_number[3]

for number_one in range(int(first_digit_first_num), int(first_digit_second_num) + 1):
    if number_one % 2 == 0:
        continue

    for number_two in range(int(second_digit_first_num), int(second_digit_second_num) + 1):
        if number_two % 2 == 0:
            continue

        for number_three in range(int(third_digit_first_num), int(third_digit_second_num) + 1):
            if number_three % 2 == 0:
                continue

            for number_four in range(int(forth_digit_first_num), int(forth_digit_second_num) + 1):
                if number_four % 2 == 0:
                    continue

                print(f"{number_one}{number_two}{number_three}{number_four}", end=" ")
