def reverse_text(word: str):
    current_index = len(word) - 1

    while current_index >= 0:
        yield word[current_index]

        current_index -= 1


for char in reverse_text("step"):
    print(char, end='')
