def gather_credits(number_of_credits, *course_data):
    current_credits = 0
    enrolled_courses = []

    for course in course_data:
        name, credit = course

        if current_credits >= number_of_credits:
            break

        if name not in enrolled_courses:
            enrolled_courses.append(name)
            current_credits += credit

    if current_credits >= number_of_credits:
        return f"Enrollment finished! Maximum credits: {current_credits}.\nCourses: {', '.join(sorted(enrolled_courses))}"

    return f"You need to enroll in more courses! You have to gather {number_of_credits - current_credits} credits more."