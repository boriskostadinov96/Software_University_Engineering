rooms = int(input())
total_chairs = 0
total_visitors = 0
is_chairs_enough = True

for current_room in range(1, rooms + 1):
    chairs, visitors = input().split()
    visitors = int(visitors)

    total_visitors += visitors
    total_chairs += len(chairs)
    free_chairs = total_chairs - total_visitors

    if len(chairs) < visitors:
        is_chairs_enough = False
        print(f"{visitors - len(chairs)} more chairs needed in room {current_room}")

if is_chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")

# solution 2

# def check_the_rooms(number_of_rooms):
#     free_chairs = 0
#
#     for number_of_room in range(1, number_of_rooms + 1):
#         free_chairs_in_current_room, visitors = input().split()
#         difference = len(free_chairs_in_current_room) - int(visitors)
#
#         if difference < 0:
#             print(f"{abs(difference)} more chairs needed in room {number_of_room}")
#         free_chairs += difference
#
#     return free_chairs
#
#
# count_of_rooms = int(input())
# total_free_chairs = check_the_rooms(count_of_rooms)
#
# if total_free_chairs >= 0:
#     print(f"Game On, {total_free_chairs} free chairs left")