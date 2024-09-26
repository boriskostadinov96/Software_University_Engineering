count = int(input())
records = {}

for _ in range(count):
    students_data = input().split()
    student_name = students_data[0]
    grade = float(students_data[1])

    if student_name not in records:
        records[student_name] = [grade]
    else:
        records[student_name].append(grade)

for key, value in records.items():
    avg_grade = sum(value) / len(value)
    formatted_grades = ' '.join(f"{g:.2f}" for g in value)
    print(f"{key} -> {formatted_grades} (avg: {avg_grade:.2f})")
