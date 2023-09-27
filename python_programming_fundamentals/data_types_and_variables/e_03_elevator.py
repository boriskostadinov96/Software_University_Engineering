# from math import ceil
#
# people_number = int(input())
# capacity = int(input())
#
# courses = ceil(people_number / capacity)
# print(courses)

persons = int(input())
capacity = int(input())
courses = 0

while persons > 0:
    persons -= capacity
    courses += 1
print(courses)
