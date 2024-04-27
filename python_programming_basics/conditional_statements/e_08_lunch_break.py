import math

serial_name = input()
episode_duration = int(input())
rest_duration = int(input())

lunch_time = rest_duration / 8
relax_time = rest_duration / 4

total_time = rest_duration - (lunch_time + relax_time)

if total_time >= episode_duration:
    print(
        f"You have enough time to watch {serial_name} and left with {math.ceil(total_time - episode_duration)} minutes free time.")

else:
    print(
        f"You don't have enough time to watch {serial_name}, you need {math.ceil(episode_duration - total_time)} more minutes.")
