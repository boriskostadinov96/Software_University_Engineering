from collections import deque


def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    cubes = deque(args)

    while cubes[0] != "Finish":
        first_cube = cubes.popleft()

        if box_size >= first_cube:
            box_size -= first_cube

        else:
            diff = first_cube  - box_size
            cubes.appendleft(diff)

            sum_nums = sum(n for n in cubes if n != 'Finish')
            return f"No more free space! You have {sum_nums} more cubes."

    return f"There is free space in the box. You could put {box_size} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

# better solution
# from collections import deque
# def fill_the_box(height, length, width, *cubes):
#     cube_volume = height * length * width
#     cubes = deque(cubes)
#
#     while cubes[0] != "Finish":
#         cube_volume -= cubes.popleft()
#
#         if cube_volume < 0:
#             cubes_left = sum(c for c in cubes if c != "Finish")
#             return f"No more free space! You have {cubes_left + abs(cube_volume)} more cubes."
#
#     return f"There is free space in the box. You could put {cube_volume} more cubes."