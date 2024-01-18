count_of_input_lines = int(input())
periodic_table = set()

for _ in range(count_of_input_lines):
    for chemical in input().split():
        periodic_table.add(chemical)

print(*periodic_table, sep="\n")