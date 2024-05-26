integers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    smallest_num = min(integers)
    integers.remove(smallest_num)

print(*integers, sep=", ")

# solution 2
# string = input()
# counter = int(input())
#
# list_of_numbers = string.split(' ')
# list_of_numbers = list(map(lambda x: int(x), list_of_numbers))
#
# for i in range(counter):
#     smallest = min(list_of_numbers)
#     list_of_numbers.remove(smallest)
#
# list_of_numbers = list(map(lambda x: str(x), list_of_numbers))
# print(", ".join(list_of_numbers))
