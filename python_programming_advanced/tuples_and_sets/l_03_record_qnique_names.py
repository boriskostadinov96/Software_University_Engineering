names_count = int(input())
unique_names = set()

for _ in range(names_count):
    current_name = input()
    unique_names.add(current_name)

for unique_name in unique_names:
    print(unique_name)