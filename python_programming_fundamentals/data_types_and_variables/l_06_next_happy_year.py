current_year = int(input())

while True:
    current_year += 1

    if len(set(str(current_year))) == len(str(current_year)):
        print(current_year)
        break

# solution 2
# year = int(input())
# year_is_special = False
#
# while not year_is_special:
#     year += 1
#     year_as_string = str(year)
#     year_is_special = True
#
#     for digit in year_as_string:
#
#         if year_as_string.count(digit) > 1:
#             year_is_special = False
#             break
#
# print(year)