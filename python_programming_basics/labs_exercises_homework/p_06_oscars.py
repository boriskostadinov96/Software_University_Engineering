def calculate_points(actor_name, academy_points, num_reviewers):
    total_points = academy_points

    for _ in range(num_reviewers):
        reviewer_name = input()
        reviewer_points = float(input())

        total_points += len(reviewer_name) * reviewer_points / 2

        if total_points > 1250.5:
            print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
            return

    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")


actor_name = input()
academy_points = float(input())
num_reviewers = int(input())

calculate_points(actor_name, academy_points, num_reviewers)
