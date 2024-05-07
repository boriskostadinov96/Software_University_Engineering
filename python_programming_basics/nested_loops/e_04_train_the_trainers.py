jury_count = int(input())
presentation = input()
total_average_grade = 0
presentation_count = 0

while presentation != "Finish":
    presentation_average = 0

    for _ in range(jury_count):
        current_grade = float(input())
        presentation_average += current_grade

    presentation_average /= jury_count
    total_average_grade += presentation_average
    presentation_count += 1

    print(f"{presentation} - {presentation_average:.2f}.")

    presentation = input()

final_average_grade = total_average_grade / presentation_count
print(f"Student's final assessment is {final_average_grade:.2f}.")
