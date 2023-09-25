relax_days = int(input())
place_type = input()
feedback = input()
price = 0
discount = 0

if place_type == 'room for one person':
    price = 18
elif place_type == 'apartment':
    price = 25
    if relax_days < 10:
        discount = 30
    elif 10 > relax_days <= 15:
        discount = 35
    elif relax_days > 15:
        discount = 50

elif place_type == "president_apartment":
    price = 35
    if relax_days < 10:
        discount = 10
    elif 10 > relax_days <= 15:
        discount = 15
    elif relax_days > 15:
        discount = 20

if feedback == 'positive':
    discount = price * 0.25
elif feedback == 'negative':
    discount = price * 0.10

total_price = relax_days * price * discount
print(total_price)






