from __future__ import annotations
from abc import ABC
from typing import TypeVar, Optional

from procedural_cuisine.ingredients import Ingredient, State
from procedural_cuisine.units import Length, AMOUNT_UNIT

CONCRETE_INGREDIENT = TypeVar("CONCRETE_INGREDIENT", bound=Ingredient)


class Utensil(ABC):
    ...


class Container(Utensil, ABC):
    def __init__(self):
        self.contents = set()

    # move
    def transfer_to(self, value: float, unit: AMOUNT_UNIT, container: Container):
        ...

    def transfer_all_to(self, container: Container):
        ...

    def add(self, *ingredients: CONCRETE_INGREDIENT):
        for each_ingredient in ingredients:
            self.contents.add(each_ingredient)

    # agitate
    def stir(self):
        ...

    def fold(self):
        ...

    def whisk(self):
        ...

    # read
    def contents(self) -> set[CONCRETE_INGREDIENT]:
        ...

    def state_content(self) -> set[State]:
        ...


class ServingContainer(Container):
    def sprinkle_with(self, ingredient: Ingredient, value: float, unit: AMOUNT_UNIT):
        ...


class Bowl(ServingContainer):
    ...


class MortarNPestle(Container):
    def pound(self):
        ...


class Pot(Container):
    def __init__(self, minimum_diameter: Optional[Length] = None):
        super().__init__()
        self.minimum_diameter = minimum_diameter
        self.heat = 0.

    def set_heat(self, value: float):
        self.heat = value
