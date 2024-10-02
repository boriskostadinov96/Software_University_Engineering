def age_assignment(*names, **people):
    result = {}

    for key, value in people.items():
        for name in names:
            letter = name[0]

            if letter == key:
                result[name] = value

    sorted_names = sorted(result.items(), key=lambda x: x)
    return '\n'.join(f"{n} is {y} years old." for n, y in sorted_names)

print(age_assignment("Peter", "George", G=26, P=19))

# a better solution 
# def age_assignment(*names, **age_data):
#     result = []
#
#     for letter, age in age_data.items():
#         for name in names:
#             if name.startswith(letter):
#                 result.append(f"{name} is {age} years old.")
#                 break
#
#     return "\n".join(sorted(result))
#
# print(age_assignment("Peter", "George", G=26, P=19))