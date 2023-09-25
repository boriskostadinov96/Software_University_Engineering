hall_rent = int(input())

oscars_price = hall_rent - (hall_rent * 0.30)
katering_price = oscars_price - (oscars_price * 0.15)
sounding_price = katering_price / 2

total_price = hall_rent + oscars_price + katering_price + sounding_price

print(f'{total_price:.2f}')
