numbers_file = open("numbers.txt")
total_sum = 0

for n in numbers_file:
    total_sum += int(n.strip())

print(total_sum)

# 1.1
# import os.path
#
# path = os.path.join("resources", "numbers.txt")
#
# file = open(path)
#
# total_amount = 0
# lines = file.readlines()
# file.close()
#
# for line in lines:
#     total_amount += int(line.strip())
#
# print(total_amount)