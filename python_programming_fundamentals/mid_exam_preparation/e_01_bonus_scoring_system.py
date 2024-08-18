import math

students_count = int(input())
total_lectures = int(input())
additional_bonus = int(input())
highest_score = float('-inf')

for current_student in range(students_count):
    attendance = int(input())

    total_bonus = attendance / total_lectures * (5 + additional_bonus)
    if total_bonus > highest_score:
        highest_score = total_bonus
        his_lectures = attendance

print(f'Max Bonus: {math.ceil(highest_score)}.')
print(f'The student has attended {his_lectures} lectures.')

