from math import sqrt


prime_sum = 0
non_prime_sum = 0

while True:
    command = input()

    if command == "stop":
        break

    current_number = int(command)

    if current_number < 0:
        print("Number is negative.")
        continue

    for number in range(2, int(sqrt(current_number)) + 1):
        if current_number % number == 0:
            non_prime_sum += current_number
            break

    else:
        prime_sum += current_number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")