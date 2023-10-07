def calculate_total_amount(product, quantity):
    result = 0
    if product == "coffee":
        result = quantity * 1.50

    elif product == "water":
        result = quantity * 1.00

    elif product == "coke":
        result = quantity * 1.40

    elif product == "snacks":
        result = quantity * 2.00

    return result


product_name = input()
requested_quantity = int(input())

total_amount = calculate_total_amount(product_name, requested_quantity)
print(f'{total_amount:.2f}')


