def tribonacci_numbers(num):

    if num == 0:
        return []

    elif num == 1:
        return [1]

    elif num == 2:
        return [1, 1]

    elif num == 3:
        return [1, 1, 2]

    else:
        result = tribonacci_numbers(num - 1)
        next_one = result[-3] + result[-2] + result[-1]
        result.append(next_one)

        return result


number = int(input())

tribonacci_sequence = tribonacci_numbers(number)
print(" ".join(map(str, tribonacci_sequence)))
