from procedural_cuisine.ingredients import State, Ingredient
from procedural_cuisine.meals import Meal
from procedural_cuisine.units import MassUnit, VolumeUnit, ImpreciseUnit
from procedural_cuisine.utensils import Pot, Bowl


def prepare(ingredients: dict[str, Ingredient]) -> Meal:
    # prepare your utensils
    pot = Pot()
    bowl = Bowl()

    # put all ingredients in the pot
    pot.add(*ingredients.values())

    # set pot on high heat
    pot.set_heat(1.)

    # whisk
    pot.whisk()

    # wait until content is simmering
    while State.SIMMERING not in pot.state_content():
        continue

    # turn off heat
    pot.set_heat(0.)

    # whisk
    pot.whisk()

    # transfer content into bowl
    pot.transfer_all_to(bowl)

    # let cool down
    while State.HOT in bowl.state_content():
        continue

    # serve
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
