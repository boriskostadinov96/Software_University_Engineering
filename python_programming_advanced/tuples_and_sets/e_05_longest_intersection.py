n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = [el.split(",") for el in input().split("-")]

    first_set = set(range(int(first_range[0]), int(first_range[1]) + 1))
    second_set = set(range(int(second_range[0]), int(second_range[1]) + 1))

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(
    f"Longest intersection is "
    f"[{', '.join(str(x) for x in longest_intersection)}] "
    f"with length {len(longest_intersection)}"
)