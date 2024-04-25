length = int(input())
width = int(input())
height = int(input())
percent_acc = float(input())

volume = length * width * height
total_lit = volume / 1000
acc_volume = total_lit * (percent_acc / 100)
result = total_lit - acc_volume

print(result)