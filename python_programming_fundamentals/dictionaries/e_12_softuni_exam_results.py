command = input().split('-')
result = {}
language_submissions = {}

while command[0] != "exam finished":
    username = command[0]
    language = command[1]

    if language == 'banned':
        if username in result:
            del result[username]
        command = input().split('-')
        continue

    points = int(command[2])

    if language not in language_submissions:
        language_submissions[language] = 0

    language_submissions[language] += 1

    if username not in result:
        result[username] = [language, points]

    else:
        if language in result[username]:
            lang_index = result[username].index(language)

            if points > result[username][lang_index + 1]:
                result[username][lang_index + 1] = points

        else:
            result[username].append(language)
            result[username].append(points)

    command = input().split('-')


print("Results:")
for username, data in result.items():
    total_points = sum(data[i + 1] for i in range(0, len(data), 2))
    print(f"{username} | {total_points}")

print("Submissions:")
for language, count in language_submissions.items():
    print(f"{language} - {count}")
