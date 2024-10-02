def grocery_store(**kwargs):
    sorted_grocery = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return '\n'.join(f"{p}: {q}" for p, q in sorted_grocery)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))