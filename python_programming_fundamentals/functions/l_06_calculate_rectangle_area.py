def rectangle_area(wight, height):
    area = wight * height
    return area


rectangle_wight = int(input())
rectangle_height = int(input())

total_result = rectangle_area(rectangle_wight, rectangle_height)
print(total_result)