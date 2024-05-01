actor_name = input()
total_points = float(input())
judges_count = int(input())

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    total_points += len(judge_name) * judge_points / 2

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

else:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")