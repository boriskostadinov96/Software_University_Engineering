number = int(input())

for current_number in range(1, number + 1):
    digits_sum = sum(int(digit) for digit in str(current_number))

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")