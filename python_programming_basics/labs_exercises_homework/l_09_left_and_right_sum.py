n_number = int(input())

left_sum = 0
right_sum = 0

for i in range(n_number):
    enter_left = int(input())
    left_sum += enter_left

for i in range(n_number):
    enter_right = int(input())
    right_sum += enter_right

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")