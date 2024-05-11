strings_count = int(input())

for _ in range(strings_count):
    current_str = input()

    if "," in current_str or "." in current_str or "_" in current_str:
        print(f"{current_str} is not pure!")

    else:
        print(f"{current_str} is pure.")