number_of_guests = int(input())
unique_codes = set()

for _ in range(number_of_guests):
    reservation_code = input()
    unique_codes.add(reservation_code)

code_as_command = input()
while code_as_command != "END":

    if code_as_command in unique_codes:
        unique_codes.remove(code_as_command)

    code_as_command = input()

print(len(unique_codes))

for current_code in sorted(unique_codes):
    print(current_code)