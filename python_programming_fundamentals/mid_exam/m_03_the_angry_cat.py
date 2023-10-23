items = list(map(int, input().split(", ")))
positionIdx = int(input())
type = input()
leftSum, rightSum = 0, 0
if type == "cheap":
    leftSum = sum([e for e in items[:positionIdx] if e < items[positionIdx]])
    rightSum = sum([e for e in items[positionIdx+1:] if e < items[positionIdx]])
elif type == "expensive":
    leftSum = sum([e for e in items[:positionIdx] if e >= items[positionIdx]])
    rightSum = sum([e for e in items[positionIdx+1:] if e >= items[positionIdx]])

if leftSum > rightSum:
    print(f"{'Left'} - {leftSum}")
elif rightSum > leftSum:
    print(f"{'Right'} - {rightSum}")
else:
    print(f"{'Left'} - {leftSum}")



