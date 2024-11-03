class vowels:
    def __init__(self, some_string: str):
        self.some_string = some_string
        self.vowels_list = ['a', 'e', 'i', 'u', 'y', 'o']
        self.index = - 1
        self.vowels_values = [c for c in self.some_string if c.lower() in self.vowels_list]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_values):
            return self.vowels_values[self.index]

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# solution without __next__():
# class vowels:
#     def __init__(self, some_string: str):
#         self.some_string = some_string
#         self.vowels_list = ['a', 'e', 'i', 'u', 'y', 'o']
#         self.index = -1
#         self.vowels_values = [c for c in self.some_string if c.lower() in self.vowels_list]
#
#     def __iter__(self):
#         return iter(self.vowels_values)
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
