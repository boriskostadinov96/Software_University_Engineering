chicken_menu = int(input())
fish_menu = int(input())
vegi_menu = int(input())

total_price = chicken_menu * 10.35 + fish_menu * 12.40 + vegi_menu * 8.15
desert_price = (total_price * 0.2)

final_price = total_price + desert_price + 2.5
print(final_price)