from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


color = Color.RED
print(color.name, color.value)
