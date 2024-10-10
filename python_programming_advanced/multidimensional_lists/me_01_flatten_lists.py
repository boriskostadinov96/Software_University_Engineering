text = input().split("|")
flatten_list = []

for element in text[::-1]:
    flatten_list.extend(element.split())

print(*flatten_list)

# solution 2
# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])