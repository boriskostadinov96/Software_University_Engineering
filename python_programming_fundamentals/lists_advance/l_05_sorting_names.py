name = input().split(", ")
sorted_list = sorted(name, key=lambda x: (-len(x), x))
print(sorted_list)