even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    names = input()
    ascii_sum_of_name = sum(ord(letter) for letter in names) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)

    else:
        odd_set.add(ascii_sum_of_name)

sum_of_even_set = sum(even_set)
sum_of_odd_set = sum(odd_set)

if sum_of_even_set == sum_of_odd_set:
    print(*odd_set.union(even_set), sep=", ")

elif sum_of_even_set < sum_of_odd_set:
    print(*odd_set.difference(even_set), sep=", ")

else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")

# solution 2
# n = int(input())
# letters_sum = 0
# even_set = set()
# odd_set = set()
#
# for row in range(1, n + 1):
#     names = input()
#     letters_sum = 0
#
#     for letter in names:
#         letters_sum += (ord(letter))
#     letters_sum = letters_sum // row
#
#     if letters_sum % 2 == 0:
#         even_set.add(letters_sum)
#
#     else:
#         odd_set.add(letters_sum)
#
# even_sum = sum(even_set)
# odd_sum = sum(odd_set)
#
# if odd_sum == even_sum:
#     print(*odd_set.union(even_set), sep=", ")
#
# elif even_sum > odd_sum:
#     print(*odd_set.symmetric_difference(even_set), sep=", ")
#
# elif odd_sum > even_sum:
#     print(*odd_set.difference(even_set), sep=", ")


