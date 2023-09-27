number = int(input())

for current_number in range(number):
    numbers = int(input())
    if numbers % 2 != 0:
        print(f'{numbers } is odd!')
        break

else:
    print(f"All numbers are even.")