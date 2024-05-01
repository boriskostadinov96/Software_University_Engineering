tournaments_count = int(input())
starting_points = int(input())
w_points = 2000
f_points = 1200
sf_points = 720
final_points = 0
winning_tournaments = 0

for _ in range(tournaments_count):
    current_stage = input()

    if current_stage == "W":
        final_points += w_points
        winning_tournaments += 1

    elif current_stage == "F":
        final_points += f_points

    elif current_stage == "SF":
        final_points += sf_points


final_points += starting_points
average_points = (final_points - starting_points) // tournaments_count
winning_tournaments = (winning_tournaments / tournaments_count) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{winning_tournaments:.2f}%")