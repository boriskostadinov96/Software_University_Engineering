from collections import deque

sequence_of_parentheses = deque(input())
opening_parentheses = deque()

while sequence_of_parentheses:
    current_parentheses = sequence_of_parentheses.popleft()

    if current_parentheses in "({[":
        opening_parentheses.append(current_parentheses)

    elif not opening_parentheses:
        print("NO")
        break

    else:
        if f"{opening_parentheses.pop() + current_parentheses}" not in "()[]{}":
            print("NO")
            break

else:
    print("YES")