count_of_usernames = int(input())
unique_usernames = set()

for _ in range(count_of_usernames):
    username = input()

    if username not in unique_usernames:
        unique_usernames.add(username)

for current_username in unique_usernames:
    print(current_username)