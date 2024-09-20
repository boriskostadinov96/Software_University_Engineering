clothes = [int(x) for x in input().split()]
capacity = int(input())
total_racks = 1
rack_space = capacity

while clothes:
    current_cloth = clothes.pop()

    if rack_space >= current_cloth:
        rack_space -= current_cloth

    else:
        total_racks += 1
        rack_space = capacity - current_cloth

print(total_racks)