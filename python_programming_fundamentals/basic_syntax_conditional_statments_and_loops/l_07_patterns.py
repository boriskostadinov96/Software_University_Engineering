max_stars_per_count = int(input())

for i in range(1, max_stars_per_count + 1):

    for j in range(i):
        print("*", end="")

    print()

for i in range(max_stars_per_count - 1, 0, - 1):

    for j in range(i):
        print("*", end="")

    print()