def multiplication(num_one, num_two, num_three):
    if num_one == 0 or num_two == 0 or num_three == 0:
        return "zero"

    elif num_one * num_two * num_three > 0:
        return "positive"

    else:
        return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication(first_number, second_number, third_number))