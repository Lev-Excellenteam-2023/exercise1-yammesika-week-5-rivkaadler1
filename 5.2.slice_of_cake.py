def get_recipe_price(prices, optionals=None, **ingredients):
    """
    Calculates the total price of the ingredients needed to make a recipe.

    Args: prices (dict): a dictionary where the keys are ingredient names and the values are prices per 100g.
    optionals (list): a list of optional ingredients to ignore. Defaults to None. **ingredients: keyword arguments
    where the keys are ingredient names and the values are the amount (in grams) needed for the recipe.

    Returns:
    The total price of all the ingredients needed for the recipe, after ignoring the optional ingredients.
    """
    total_price = 0
    for ingredient, grams in ingredients.items():
        if optionals and ingredient in optionals:
            continue
        total_price += prices[ingredient] * grams / 100
    return total_price


