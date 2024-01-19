even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(letter) for letter in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)

    else:
        odd_set.add(ascii_sum_of_name)

sum_of_even_set = sum(even_set)
sum_of_odd_set = sum(odd_set)

if sum_of_even_set == sum_of_odd_set:
    print(*odd_set.union(even_set), sep=", ")

elif sum_of_even_set < sum_of_odd_set:
    print(*odd_set.difference(even_set), sep=", ")  # B - A

else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")