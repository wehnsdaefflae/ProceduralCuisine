from __future__ import annotations
from abc import ABC
from typing import TypeVar, Optional

from procedural_cuisine.ingredients import Ingredient
from procedural_cuisine.units import Length, AMOUNT_UNIT

CONCRETE_INGREDIENT = TypeVar("CONCRETE_INGREDIENT", bound=Ingredient)


class Utensil(ABC):
    ...


class Container(Utensil, ABC):
    def __init__(self):
        self.contents = set()
        self.temperature_content_degree_celsius = 20.
        self.viscosity_content_pas = 1.

    def transfer_to(self, value: float, unit: AMOUNT_UNIT, container: Container):
        ...

    def add(self, *ingredients: CONCRETE_INGREDIENT):
        for each_ingredient in ingredients:
            self.contents.add(each_ingredient)

    def contents(self) -> set[CONCRETE_INGREDIENT]:
        ...

    def is_content_boiling(self) -> bool:
        return self.temperature_content_degree_celsius >= 100.

    def is_content_thickened(self) -> bool:
        return self.viscosity_content_pas >= 100.

    def is_content_paste(self) -> bool:
        return self.viscosity_content_pas >= 100_000.


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

    def heat(self):
        self.temperature_content_degree_celsius += 1.

    def sear(self):
        self.heat()

    def cook(self):
        self.heat()

    def simmer(self):
        if self.temperature_content_degree_celsius < 100.:
            self.heat()

        elif self.temperature_content_degree_celsius >= 20.:
            self.temperature_content_degree_celsius -= 1.

    def stir(self):
        ...

    def fold(self):
        ...
