first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time

time_in_minutes = total_time // 60
seconds = total_time % 60

print(f"{time_in_minutes}:{seconds:02d}")