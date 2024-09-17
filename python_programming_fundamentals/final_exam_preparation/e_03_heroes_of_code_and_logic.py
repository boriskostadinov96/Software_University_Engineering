count = int(input())
MAX_HP = 100
MAX_MP = 200
heroes = {}

for _ in range(count):
    data = input().split()
    name = data[0]
    health = int(data[1])
    mana = int(data[2])

    heroes[name] = [health, mana]

command = input().split(" - ")

while command[0] != "End":
    hero_name = command[1]

    if command[0] == "Heal":
        health_to_add = int(command[2])
        current_health = heroes[hero_name][0]

        healed = min(MAX_HP - current_health, health_to_add)
        heroes[hero_name][0] += healed

        print(f"{hero_name} healed for {healed} HP!")

    elif command[0] == "Recharge":
        mana_to_add = int(command[2])
        current_mana = heroes[hero_name][1]

        recharged = min(MAX_MP - current_mana, mana_to_add)
        heroes[hero_name][1] += recharged

        print(f"{hero_name} recharged for {recharged} MP!")

    elif command[0] == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]

        if heroes[hero_name][0] > damage:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)

    elif command[0] == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]

        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    command = input().split(" - ")

for key, value in heroes.items():
    print(f"{key}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
