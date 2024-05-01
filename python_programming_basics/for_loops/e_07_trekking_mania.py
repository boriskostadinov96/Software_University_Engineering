groups_of_climbers = int(input())
mussala_count = 0
monblan_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(1, groups_of_climbers + 1):
    people_count = int(input())

    if people_count <= 5:
        mussala_count += people_count

    elif 6 <= people_count <= 12:
        monblan_count += people_count

    elif 13 <= people_count <= 25:
        kilimandjaro_count += people_count

    elif 26 <= people_count <= 40:
        k2_count += people_count

    else:
        everest_count += people_count

total_climbers = mussala_count + monblan_count + kilimandjaro_count + k2_count + everest_count

mussala_percentage = mussala_count / total_climbers * 100
monblan_percentage = monblan_count / total_climbers * 100
kilimandjaro_percentage = kilimandjaro_count / total_climbers * 100
k2_percentage = k2_count / total_climbers * 100
everest_percentage = everest_count / total_climbers * 100

print(f"{mussala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimandjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")
