from src.ingredients import State, Ingredient
from src.meals import Meal
from src.units import MassUnit, VolumeUnit, ImpreciseUnit, LengthUnit, AMOUNT_UNIT, Length
from src.utensils import Pot, MortarNPestle, Bowl


def prepare(ingredients: dict[str, tuple[float, AMOUNT_UNIT, set[State]]]) -> Meal:
    """
    Heat sheep fat in a pot wide enough for the diced lamb to spread in one layer.
    Add lamb and sear on high heat until all moisture evaporates.
    Fold in the onion and keep cooking until it is almost transparent.
    Fold in salt, beetroot, rocket, fresh coriander, Persian shallot and cumin.
    Keep on folding until the moisture evaporates.
    Pour in beer, and then add water.
    Give the mixture a light stir and then bring to a boil.
    Reduce heat and add leek and garlic.
    Allow to simmer for about an hour until the sauce thickens.
    """

    pot = Pot(minimum_diameter=Length(40., LengthUnit.CENTIMETERS))

    sheep_fat = Ingredient(*ingredients["sheep fat"])
    pot.add(sheep_fat)
    while State.MELTED not in sheep_fat.state:
        pot.heat()

    lamb = Ingredient(*ingredients["leg of mutton"])
    pot.add(lamb)
    while State.MOIST in lamb.state and State.SEARED not in lamb.state:
        pot.sear()

    onion = Ingredient(*ingredients["onion"])
    pot.add(onion)
    pot.fold()
    while State.TRANSPARENT not in onion.state:
        pot.cook()

    salt = Ingredient(*ingredients["salt"])
    beetroot = Ingredient(*ingredients["beetroot"])
    rocket = Ingredient(*ingredients["rocket"])
    coriander = Ingredient(*ingredients["coriander"])
    coriander_garnish = coriander.take_from(.5, VolumeUnit.CUPS)
    persian_shallot = Ingredient(*ingredients["persian shallot"])
    cumin_seeds = Ingredient(*ingredients["cumin seeds"])

    pot.add(salt, beetroot, rocket, coriander, persian_shallot, cumin_seeds)
    while any(State.MOIST in x.state for x in pot.contents()):
        pot.fold()
        pot.cook()

    sour_beer = Ingredient(*ingredients["sour beer"])
    german_beer = Ingredient(*ingredients["German Weißbier"])
    pot.add(sour_beer, german_beer)

    water = Ingredient(*ingredients["water"])
    pot.add(water)

    pot.stir()
    while not pot.is_content_boiling():
        pot.cook()

    leek = Ingredient(*ingredients["leek"])
    garlic = Ingredient(*ingredients["garlic cloves"])
    pot.add(leek, garlic)

    while not pot.is_content_thickened():
        pot.simmer()

    """
    Pound kurrat and remaining fresh coriander into a paste using a mortar and pestle.
    Ladle the stew into bowls and sprinkle with coriander seeds and kurrat and fresh coriander paste.
    The dish can be served with steamed bulgur, boiled chickpeas and bread.
    """
    kurrat = Ingredient(*ingredients["kurrat or spring leek"])
    mortar = MortarNPestle()
    mortar.add(kurrat, coriander_garnish)
    while not mortar.is_content_paste():
        mortar.pound()

    bowl = Bowl()
    pot.transfer_to(1, ImpreciseUnit.SERVING, bowl)
    mortar.transfer_to(1., ImpreciseUnit.ALL, bowl)

    coriander_seeds = Ingredient(*ingredients["coriander seeds"])
    bowl.sprinkle_with(coriander_seeds, coriander_seeds.amount.value, coriander_seeds.amount.unit)

    return Meal(bowl)


def main():
    # https://www.bbc.com/travel/article/20191103-the-worlds-oldest-known-recipes-decoded

    ingredients = {
        "leg of mutton":            (1., MassUnit.POUND, {State.DICED}),
        "sheep fat":                (.5, VolumeUnit.CUPS, {State.MELTED}),
        "onion":                    (1., ImpreciseUnit.SMALL, {State.CHOPPED}),
        "salt":                     (.5, ImpreciseUnit.TEASPOONS, {State.DEFAULT}),
        "beetroot":                 (1., MassUnit.POUND, {State.PEELED, State.DICED}),
        "rocket":                   (1., VolumeUnit.CUPS, {State.CHOPPED}),
        "coriander":                (1., VolumeUnit.CUPS, {State.FRESH}),   # todo: finely chop .5 cup for garnish
        "persian shallot":          (1., VolumeUnit.CUPS, {State.CHOPPED}),
        "cumin seeds":              (1., ImpreciseUnit.TEASPOONS, {State.DEFAULT}),
        "sour beer":                (.5, VolumeUnit.CUPS, {State.DEFAULT}),
        "German Weißbier":          (.5, VolumeUnit.CUPS, {State.DEFAULT}),
        "water":                    (.5, VolumeUnit.CUPS, {State.DEFAULT}),
        "leek":                     (.5, VolumeUnit.CUPS, {State.CHOPPED}),
        "garlic cloves":            (2., ImpreciseUnit.PIECES, {State.PEELED, State.CRUSHED}),
        "kurrat or spring leek":    (.5, VolumeUnit.CUPS, {State.CHOPPED_FINELY}),
        "coriander seeds":          (2., ImpreciseUnit.TEASPOONS, {State.CRUSHED_COARSELY}),

    }

    meal = prepare(ingredients)
    print(meal)


if __name__ == "__main__":
    main()
