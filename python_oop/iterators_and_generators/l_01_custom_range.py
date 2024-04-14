class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current_digit = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_digit += 1

        if self.current_digit <= self.end:
            return self.current_digit

        raise StopIteration


one_to_ten = custom_range(1, 10)

for num in one_to_ten:
    print(num)
