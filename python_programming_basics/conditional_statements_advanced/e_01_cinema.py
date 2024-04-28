movie_type = input()
rows = int(input())
cols = int(input())
result = 0

area = rows * cols

if movie_type == "Premiere":
    result = area * 12

elif movie_type == "Normal":
    result = area * 7.5

elif movie_type == "Discount":
    result = area * 5

print(f"{result:.2f} leva")

