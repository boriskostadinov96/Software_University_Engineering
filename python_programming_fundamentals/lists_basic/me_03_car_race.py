car_time = [int(x) for x in input().split()]
left_racer_time = 0
right_racer_time = 0
left_racer = None
right_racer = None

for current_time in car_time:
    finish_line = len(car_time) // 2

    left_racer = car_time[:finish_line]
    right_racer = car_time[finish_line + 1:]

for idx in left_racer:
    if idx == 0:
        left_racer_time *= 0.8

    left_racer_time += idx

for el_idx in right_racer:
    if el_idx == 0:
        right_racer_time *= 0.8

    right_racer_time += el_idx

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")

else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")

# solution 2
# list_of_times = input().split(" ")
#
# left_player = list_of_times[:len(list_of_times) // 2]
# right_player = list_of_times[(len(list_of_times) // 2) + 1:]
# right_player.reverse()
#
#
# def total_time(player):
#     sum_of_times = 0
#     for number in player:
#         sum_of_times += int(number)
#         if number == "0":
#             sum_of_times *= 0.80
#     return sum_of_times
#
#
# left_player_time = total_time(left_player)
# right_player_time = total_time(right_player)
#
# if left_player_time < right_player_time:
#     print(f"The winner is left with total time: {left_player_time:.1f}")
# else:
#     print(f"The winner is right with total time: {right_player_time:.1f}")

# solution 3
# car_times = [int(x) for x in input().split()]
#
# finish_line = len(car_times) // 2
#
# left_racer_time = 0
# right_racer_time = 0
# 
# for idx in range(finish_line):
#     if car_times[idx] == 0:
#         left_racer_time *= 0.8
#     left_racer_time += car_times[idx]
#
# for idx in range(len(car_times) - 1, finish_line, -1):
#     if car_times[idx] == 0:
#         right_racer_time *= 0.8
#     right_racer_time += car_times[idx]
#
# if left_racer_time < right_racer_time:
#     print(f"The winner is left with total time: {left_racer_time:.1f}")
# else:
#     print(f"The winner is right with total time: {right_racer_time:.1f}")
