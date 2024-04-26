from math import pi

figure = input()
area = ""

if figure == "square":
    a = float(input())
    area = a * a

elif figure == "rectangle":
    a = float(input())
    b = float(input())

    area = a * b

elif figure == "circle":
    radios = float(input())

    area = pi * radios ** 2

elif figure == "triangle":
    a = float(input())
    b = float(input())

    area = a * b / 2

print(f'{area:.3f}')
