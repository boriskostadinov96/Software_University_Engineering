fruit_name = input().split()
fruits = [fruit_name for fruit_name in fruit_name if len(fruit_name) % 2 == 0]
print("\n".join(fruits))