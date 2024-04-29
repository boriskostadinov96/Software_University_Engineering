numbers = int(input())
left_sum = 0
right_sum = 0

for _ in range(numbers):
    left_nums = int(input())
    left_sum += left_nums


for _ in range(numbers):
    right_nums = int(input())
    right_sum += right_nums

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")

else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
