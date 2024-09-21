from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while cups and bottles:
    last_bottle = bottles.pop()
    current_cup = cups.popleft()

    if last_bottle >= current_cup:
        wasted_water += last_bottle - current_cup

    else:
        cups.appendleft(current_cup - last_bottle)

if cups:
    print(f"Cups:", *cups)
else:
    print(f"Bottles:", *bottles)

print(f"Wasted litters of water: {wasted_water}")
