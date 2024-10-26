def cookbook(*args):
    data_products = {}
    for product, cuisine, ingredients in args:
        if cuisine not in data_products:
            data_products[cuisine] = []
        data_products[cuisine].append((product, ingredients))

    sorted_cuisines = sorted(data_products.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for cuisine, recipes in sorted_cuisines:
        sorted_recipes = sorted(recipes)
        result += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"

        for recipe, recipe_ingredients in sorted_recipes:
            ingredients_str = ', '.join(recipe_ingredients)
            result += f"  * {recipe} -> Ingredients: {ingredients_str}\n"

    return result.strip()