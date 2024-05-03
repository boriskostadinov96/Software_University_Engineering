GOAL = 10_000
total_steps = 0

while total_steps < GOAL:
    steps = input()

    if steps == "Going home":
        total_steps += int(input())
        break

    total_steps += int(steps)

if total_steps >= GOAL:
    print(f"Goal reached! Good job!\n{total_steps - GOAL} steps over the goal!")

else:
    print(f"{GOAL - total_steps} more steps to reach goal.")