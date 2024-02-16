from collections import deque

time = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]
darth_vader_ducks = 0
thor_ducks = 0
big_blue_ducks = 0
small_yellow_ducks = 0

while time and tasks:
    first_time = time.popleft()
    last_task = tasks.pop()

    result = first_time * last_task

    if 0 <= result <= 60:
        darth_vader_ducks += 1

    elif 61 <= result <= 120:
        thor_ducks += 1

    elif 121 <= result <= 180:
        big_blue_ducks += 1

    elif 181 <= result <= 240:
        small_yellow_ducks += 1

    else:
        last_task -= 2
        tasks.append(last_task)
        time.append(first_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"""Darth Vader Ducky: {darth_vader_ducks}
Thor Ducky: {thor_ducks}
Big Blue Rubber Ducky: {big_blue_ducks}
Small Yellow Rubber Ducky: {small_yellow_ducks}
""")