chicken_menu = int(input())
fish_menu = int(input())
vegeterian_menu = int(input())

price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_vegeterian_menu = vegeterian_menu * 8.15

all_menu_price = price_chicken_menu + price_fish_menu + price_vegeterian_menu

desert_price = (all_menu_price * 0.20)

total_price = all_menu_price + desert_price + 2.50
print(total_price)
