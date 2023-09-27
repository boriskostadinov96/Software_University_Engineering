current_hour = int(input())
week_day = input()

if week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or \
        week_day == 'Thursday' or week_day == 'Friday' or week_day == 'Saturday':
    if 10 <= current_hour <= 18:
        print('open')
    else:
        print('closed')

else:
    print('closed')
