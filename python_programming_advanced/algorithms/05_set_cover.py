def set_cover(universe, all_sets):
    chosen_sets = []

    while universe:
        best_set = max(all_sets, key=lambda s: len(universe.intersection(s)))
        chosen_sets.append(best_set)
        universe -= best_set
        all_sets.remove(best_set)

    return chosen_sets


universe = {int(x) for x in input().split(', ')}
count = int(input())
all_sets = [{int(x) for x in input().split(', ')} for _ in range(count)]

result = set_cover(universe, all_sets)

for i in range(len(result)):
    result[i] = sorted(result[i])

print(f"Sets to take ({len(result)}):")
[print("{ " + f"{', '.join(map(str, s))}" + " }") for s in result]
