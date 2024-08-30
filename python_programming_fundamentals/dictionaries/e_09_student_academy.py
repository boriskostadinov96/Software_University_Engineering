n = int(input())
result = {}

for _ in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in result.keys():
        result[student_name] = []

    result[student_name].append(student_grade)

for key, value in result.items():
    final_grade = sum(result[key]) / len(value)

    if final_grade >= 4.50:
        print(f"{key} -> {final_grade:.2f}")


# solution 2
# pairs = int(input())
# students = {}
#
# for pair in range(pairs):
#     name = input()
#     grade = float(input())
#     if name not in students:
#         students[name] = [grade]
#     else:
#         students[name].append(grade)
#
# for student in students:
#     students[student] = sum(students[student]) / len(students[student])
#
# filtered_students = {student: avg for student, avg in students.items() if avg >= 4.50}
#
# for name, grade in filtered_students.items():
#     print(f"{name} -> {grade:.2f}")
