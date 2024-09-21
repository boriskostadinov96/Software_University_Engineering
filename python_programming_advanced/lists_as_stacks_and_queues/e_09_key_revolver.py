from collections import deque

price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])
intelligence_value = int(input())

bullets_in_barrel = gun_barrel_size
total_bullets_fired = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    total_bullets_fired += 1
    bullets_in_barrel -= 1

    if bullets_in_barrel == 0 and bullets:
        print("Reloading!")
        bullets_in_barrel = gun_barrel_size

if not locks:
    bullets_left = len(bullets)
    money_earned = intelligence_value - (total_bullets_fired * price_of_bullet)
    print(f"{bullets_left} bullets left. Earned ${money_earned}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
