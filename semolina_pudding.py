from procedural_cuisine.ingredients import State, Ingredient
from procedural_cuisine.meals import Meal
from procedural_cuisine.units import MassUnit, VolumeUnit, ImpreciseUnit
from procedural_cuisine.utensils import Pot, Bowl


def prepare(ingredients: dict[str, Ingredient]) -> Meal:
    pot = Pot()
    bowl = Bowl()

    pot.add(*ingredients.values())

    pot.set_heat(1.)

    pot.whisk()
    while State.SIMMERING not in pot.state_content():
        continue

    pot.set_heat(0.)
    pot.whisk()

    pot.transfer_all_to(bowl)

    while State.HOT in bowl.state_content():
        continue

    return Meal(bowl)


def main():
    ingredients_required = {
        "milk":     (.25, VolumeUnit.LITERS, {State.DEFAULT}),
        "semolina": (25, MassUnit.GRAMS, {State.DEFAULT}),
        "cinnamon": (1., ImpreciseUnit.TEASPOONS, {State.DEFAULT}),
        "sugar":    (25., MassUnit.GRAMS, {State.DEFAULT}),
        "salt":     (1., ImpreciseUnit.PINCH, {State.DEFAULT})
    }

    ingredients_available = {k: Ingredient(*v) for k, v in ingredients_required.items()}

    meal = prepare(ingredients_available)
    print(meal)


if __name__ == "__main__":
    main()
