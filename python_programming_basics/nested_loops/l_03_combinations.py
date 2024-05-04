number = int(input())
valid_combinations = 0

for first_num in range(0, number + 1):
    for second_num in range(0, number + 1):
        for third_num in range(0, number + 1):
            result = first_num + second_num + third_num
            if result == number:
                valid_combinations += 1

print(valid_combinations)
