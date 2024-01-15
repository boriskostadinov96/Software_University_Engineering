students_count = int(input())

student_record = {}

for _ in range(students_count):
    student_name, grade_as_string = tuple(input().split())
    grade = float(grade_as_string)

    if student_name not in student_record:
        student_record[student_name] = []
    student_record[student_name].append(grade)

for name, grades in student_record.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = ' '.join([f'{g:.2f}' for g in grades])
    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")
