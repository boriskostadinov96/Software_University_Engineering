first_str = input()
second_str = input()
repeated_str = first_str

for char_idx in range(len(first_str)):
    left_part = second_str[:char_idx + 1]
    right_part = first_str[char_idx + 1:]

    new_str = left_part + right_part

    if new_str != repeated_str:
        print(new_str)
        repeated_str = new_str