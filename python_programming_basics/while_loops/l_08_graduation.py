student_name = input()
current_class = 1
bad_grades = 0
average_grade = 0
failed = False

while current_class <= 12:
    year_grade = float(input())

    if year_grade < 4:
        bad_grades += 1
        if bad_grades > 1:
            failed = True
            break
        continue

    current_class += 1
    average_grade += year_grade / 12

if failed:
    print(f"{student_name} has been excluded at {current_class} grade")

else:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

