def calculate_orders(product_name, product_quantity):
    result = 0

    if product_name == 'water':
        result = product_quantity * 1.00

    elif product_name == 'coffee':
        result = product_quantity * 1.50

    elif product_name == 'coke':
        result = product_quantity * 1.40

    elif product_name == 'snacks':
        result = product_quantity * 2.00

    return result


product = input()
quantity = int(input())

print(f"{calculate_orders(product, quantity):.2f}")

# solution 2
# def orders_price(product_name: str, quantity_products: int):
#     shop_price = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
#
#     if product_name in shop_price:
#         price_per_item = shop_price[product_name]
#         total_price = price_per_item * quantity_products
#
#         return f"{total_price:.2f}"
#
#
# product = input()
# quantity = int(input())
# print(orders_price(product, quantity))
