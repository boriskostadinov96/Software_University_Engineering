class dictionary_iter:
    def __init__(self, dict_obj: dict):  # {1: "1", 2: "2"}
        self.items = list(dict_obj.items())  # dict_obj.items() => dict_items([(1, "1"), (2, "2")])
        self.index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items) -1:
            raise StopIteration

        self.index += 1
        return self.items[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# solution two, without __next__() method

# class dictionary_iter:
#     def __init__(self, dict_obj: dict):
#         self.items = list(dict_obj.items())
#
#     def __iter__(self):
#         return iter(self.items)
# 
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
