from procedural_cuisine.ingredients import State, Ingredient
from procedural_cuisine.meals import Meal
from procedural_cuisine.units import MassUnit, VolumeUnit, ImpreciseUnit, LengthUnit, AMOUNT_UNIT, Length
from procedural_cuisine.utensils import Pot, MortarNPestle, Bowl


def prepare(ingredients: dict[str, Ingredient]) -> Meal:
    pot = Pot(minimum_diameter=Length(40., LengthUnit.CENTIMETERS))
    mortar = MortarNPestle()

    pot.set_heat(1.)

    # Heat sheep fat in a pot wide enough for the diced lamb to spread in one layer.
    sheep_fat = ingredients["sheep fat"]
    pot.add(sheep_fat)
    while State.MELTED not in sheep_fat.state:
        pot.heat()

    # Add lamb and sear on high heat until all moisture evaporates.
    lamb = ingredients["leg of mutton"]
    pot.add(lamb)
    while State.MOIST in lamb.state and State.SEARED not in lamb.state:
        continue

    # Fold in the onion and keep cooking until it is almost transparent.
    onion = ingredients["onion"]
    pot.add(onion)
    pot.fold()
    while State.TRANSPARENT not in onion.state:
        continue

    # Fold in salt, beetroot, rocket, fresh coriander, Persian shallot and cumin.
    salt = ingredients["salt"]
    beetroot = ingredients["beetroot"]
    rocket = ingredients["rocket"]
    coriander = ingredients["coriander"]
    coriander_garnish = coriander.take_from(.5, VolumeUnit.CUPS)
    persian_shallot = ingredients["persian shallot"]
    cumin_seeds = ingredients["cumin seeds"]

    pot.add(salt, beetroot, rocket, coriander, persian_shallot, cumin_seeds)

    # Keep on folding until the moisture evaporates.
    while any(State.MOIST in x.state for x in pot.contents()):
        pot.fold()

    # Pour in beer, and then add water.
    sour_beer = ingredients["sour beer"]
    german_beer = ingredients["German Weißbier"]
    pot.add(sour_beer, german_beer)

    water = ingredients["water"]
    pot.add(water)

    # Give the mixture a light stir and then bring to a boil.
    pot.stir()
    while State.COOKING not in pot.state_content():
        continue

    # Reduce heat and add leek and garlic.
    pot.set_heat(.5)

    leek = ingredients["leek"]
    garlic = ingredients["garlic cloves"]
    pot.add(leek, garlic)

    # Allow to simmer for about an hour until the sauce thickens.
    while State.THICKENED not in pot.state_content():
        continue

    # Pound kurrat and remaining fresh coriander into a paste using a mortar and pestle.
    kurrat = ingredients["kurrat or spring leek"]
    mortar.add(kurrat, coriander_garnish)
    while State.PASTE not in mortar.state_content():
        mortar.pound()

    # Ladle the stew into bowls and sprinkle with coriander seeds and kurrat and fresh coriander paste.
    bowl = Bowl()
    pot.transfer_to(1, ImpreciseUnit.SERVING, bowl)
    mortar.transfer_to(1., ImpreciseUnit.SERVING, bowl)

    coriander_seeds = ingredients["coriander seeds"]
    bowl.sprinkle_with(coriander_seeds, coriander_seeds.amount.value, coriander_seeds.amount.unit)

    return Meal(bowl)


def main():
    # https://www.bbc.com/travel/article/20191103-the-worlds-oldest-known-recipes-decoded

    names_ingredients = {
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

    # The dish can be served with steamed bulgur, boiled chickpeas and bread.
    meal = prepare({k: Ingredient(*v) for k, v in names_ingredients.items()})
    print(meal)


if __name__ == "__main__":
    main()
