n = int(input())
all_nums = []
p_one_count = 0
p_two_count = 0
p_three_count = 0
p_four_count = 0
p_five_count = 0

for _ in range(n):
    number = int(input())
    all_nums.append(number)

    if number < 200:
        p_one_count += 1

    elif 200 <= number <= 399:
        p_two_count += 1

    elif 400 <= number <= 599:
        p_three_count += 1

    elif 600 <= number <= 799:
        p_four_count += 1

    else:
        p_five_count += 1

p_one_percentage = p_one_count / n * 100
p_two_percentage = p_two_count / n * 100
p_three_percentage = p_three_count / n * 100
p_four_percentage = p_four_count / n * 100
p_five_percentage = p_five_count / n * 100

print(f"{p_one_percentage:.2f}%")
print(f"{p_two_percentage:.2f}%")
print(f"{p_three_percentage:.2f}%")
print(f"{p_four_percentage:.2f}%")
print(f"{p_five_percentage:.2f}%")

#solution 2, slower

# n = int(input())
# p_one = []
# p_two = []
# p_three = []
# p_four = []
# p_five = []
#
# for _ in range(n):
#     number = int(input())
#
#     if number < 200:
#         p_one.append(number)
#
#     elif 200 <= number <= 399:
#         p_two.append(number)
#
#     elif 400 <= number <= 599:
#         p_three.append(number)
#
#     elif 600 <= number <= 799:
#         p_four.append(number)
#
#     else:
#         p_five.append(number)
#
# p_one_percentage = len(p_one) / n * 100
# p_two_percentage = len(p_two) / n * 100
# p_three_percentage = len(p_three) / n * 100
# p_four_percentage = len(p_four) / n * 100
# p_five_percentage = len(p_five) / n * 100
#
#
# print(f"{p_one_percentage:.2f}%")
# print(f"{p_two_percentage:.2f}%")
# print(f"{p_three_percentage:.2f}%")
# print(f"{p_four_percentage:.2f}%")
# print(f"{p_five_percentage:.2f}%")

#solution 2

# number = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
#
# for num in range(number):
#     current_number = int(input())
#
#     if current_number < 200:
#         p1 += 1
#
#     elif current_number < 400:
#         p2 += 1
#
#     elif current_number < 600:
#         p3 += 1
#
#     elif current_number < 800:
#         p4 += 1
#
#     else:
#         p5 += 1
#
# p1_percentage = p1 / number * 100
# p2_percentage = p2 / number * 100
# p3_percentage = p3 / number * 100
# p4_percentage = p4 / number * 100
# p5_percentage = p5 / number * 100
#
# print(f'{p1_percentage:.2f}%')
# print(f'{p2_percentage:.2f}%')
# print(f'{p3_percentage:.2f}%')
# print(f'{p4_percentage:.2f}%')
# print(f'{p5_percentage:.2f}%')