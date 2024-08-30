command = input()
students = {}

while command != "end":
    course_name, student_names = command.split(" : ")

    if course_name not in students.keys():
        students[course_name] = []

    students[course_name].append(student_names)

    command = input()

for course_name, students_list in students.items():
    print(f"{course_name}: {len(students_list)}")

    for student in students_list:
        print(f"-- {student}")