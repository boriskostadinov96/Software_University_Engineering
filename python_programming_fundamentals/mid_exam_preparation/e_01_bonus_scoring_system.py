from math import ceil

number_of_the_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus_points = 0
student_attendances = 0

for each_student in range(number_of_the_students):
    count_of_attendances = int(input())

    total_bonus = count_of_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        student_attendances = count_of_attendances
print(f"Max Bonus: {ceil(max_bonus_points)}.")
print(f"The student has attended {student_attendances} lectures.")