def odd_even_digits_sum(num):
    even_sum = 0
    odd_sum = 0

    for digit in num:
        digit = int(digit)

        if digit % 2 == 0:
            even_sum += digit

        else:
            odd_sum += digit

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()
odd_even_digits_sum(number)
