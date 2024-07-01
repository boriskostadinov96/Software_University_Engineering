# first_sequence = input().split(', ')
# second_sequence = input().split(', ')
# substrings = []
#
# for s1 in first_sequence:
#     for s2 in second_sequence:
#         if s1 in s2:
#             substrings.append(s1)
#             break
#
# print(substrings)

# solution 2
# first_sequence = input().split(', ')
# second_sequence = input().split(', ')
# print([first_str for first_str in first_sequence if any(first_str in second_str for second_str in second_sequence)])