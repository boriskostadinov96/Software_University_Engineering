animal = input()
reptiles = ["crocodile", "tortoise", "snake"]

if animal == "dog":
    print("mammal")

elif animal in reptiles:
    print("reptile")

else:
    print("unknown")