n = int(input())
unique_elements = set()

for _ in range(n):
    chemicals = input().split()

    for el in chemicals:
        unique_elements.add(el)

print(*unique_elements, sep='\n')

# solution 2
# count_of_input_lines = int(input())
# periodic_table = set()
#
# for _ in range(count_of_input_lines):
#     for chemical in input().split():
#         periodic_table.add(chemical)
#
# print(*periodic_table, sep="\n")