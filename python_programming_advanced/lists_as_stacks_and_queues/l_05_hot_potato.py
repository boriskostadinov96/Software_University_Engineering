from collections import deque

kids_names = deque(input().split())
toss_counter = int(input()) - 1  # in which the child leaves the game !

while len(kids_names) > 1:
    kids_names.rotate(-toss_counter)
    removed_kid = kids_names.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids_names.popleft()}")
