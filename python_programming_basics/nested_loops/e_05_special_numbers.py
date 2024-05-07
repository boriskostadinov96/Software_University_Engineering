number = int(input())

for current_number in range(11_11, 10_000):
    for digit in str(current_number):
        if int(digit) == 0 or number % int(digit) != 0:
            break

    else:
        print(current_number, end=" ")

