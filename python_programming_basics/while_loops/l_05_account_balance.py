command = input()
total_sum = 0

while command != "NoMoreMoney":
    increase_sum = float(command)

    if increase_sum < 0:
        print("Invalid operation!")
        break

    else:
        print(f"Increase: {increase_sum:.2f}")
        total_sum += increase_sum

    command = input()

print(f"Total: {total_sum:.2f}")
