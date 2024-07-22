electrons = int(input())
shells = []

for shell in range(1, electrons + 1):
    max_electrons = 2 * shell ** 2

    if electrons >= max_electrons:
        shells.append(max_electrons)
        electrons -= max_electrons

        if electrons == 0:
            break

    else:
        shells.append(electrons)
        break

print(shells)