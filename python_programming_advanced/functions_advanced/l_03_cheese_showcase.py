def sorting_cheeses(**kwargs):
    result = ""
    sorted_result = sorted(kwargs.items(), key= lambda x: (-len(x[1]), x[0]))

    for cheese_name, pieces in sorted_result:
        result += cheese_name + "\n"

        for piece in sorted(pieces, reverse=True):
            result += f"{piece}" + "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
