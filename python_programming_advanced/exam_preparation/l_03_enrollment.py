def gather_credits(credits_needed, *course_data):
    enrolled_courses = []
    starting_credits = 0

    for course_name, current_credits in course_data:
        if starting_credits >= credits_needed:
            break

        if not course_name in enrolled_courses:
            enrolled_courses.append(course_name)
            starting_credits += current_credits

    if starting_credits >= credits_needed:
        return f"Enrollment finished! Maximum credits: {starting_credits}.\nCourses: {', '.join(sorted(c for c in enrolled_courses))}"

    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - starting_credits} credits more."


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
