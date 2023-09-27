day_of_week = input()
ticked_price = 0

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Friday':
    ticked_price = 12
    print(ticked_price)

elif day_of_week == 'Wednesday' or day_of_week == 'Thursday':
    ticked_price = 14
    print(ticked_price)

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    ticked_price = 16
    print(ticked_price)
