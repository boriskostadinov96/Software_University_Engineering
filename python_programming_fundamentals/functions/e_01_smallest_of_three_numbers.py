def smallest_of_three_numbers(num_one, num_two, num_three):
    if num_one < num_two and num_one < num_three:
        print(num_one)
    elif num_two < num_one and num_two < num_three:
        print(num_two)
    else:
        print(num_three)


first_num = int(input())
second_num = int(input())
third_num = int(input())

smallest_of_three_numbers(first_num, second_num, third_num)