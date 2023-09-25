time_first = int(input())
time_second = int(input())
time_third = int(input())

sum_sec = time_first + time_second + time_third

minutes = sum_sec // 60
seconds = sum_sec % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

if seconds < 10:
    print(f' {minutes}')