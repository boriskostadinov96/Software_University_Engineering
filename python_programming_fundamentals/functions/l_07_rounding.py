string_as_nums = input().split()
list_of_rounded_nums = []

for x in string_as_nums:
    # Преобразуваме низа x към float и след това го закръгляме
    rounded_num = round(float(x))
    list_of_rounded_nums.append(rounded_num)

print(list_of_rounded_nums)
