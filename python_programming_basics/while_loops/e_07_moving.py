home_width = int(input())
home_length = int(input())
home_height = int(input())
free_space = True

home_area = home_width * home_length * home_height

command = input()
while command != "Done":
    boxes = int(command)

    home_area -= boxes

    if home_area < 0:
        free_space = False
        break

    command = input()

if not free_space:
    print(f"No more free space! You need {abs(home_area)} Cubic meters more.")

else:
    print(f"{home_area} Cubic meters left.")

# solution 2
# home_width = int(input())
# home_length = int(input())
# home_height = int(input())
#
# home_area = home_width * home_length * home_height
#
# sum_boxes = 0
# command = input()
#
# while command != "Done":
#     boxes = int(command)
#     sum_boxes += boxes
#
#     if sum_boxes > home_area:
#         break
#
#     command = input()
#
# print(
#     f"No more free space! You need {abs(sum_boxes - home_area)} Cubic meters more." if sum_boxes > home_area else f"{home_area - sum_boxes} Cubic meters left.")
