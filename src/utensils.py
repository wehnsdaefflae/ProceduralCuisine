from __future__ import annotations
from abc import ABC
from typing import TypeVar, Optional

from src.ingredients import Ingredient
from src.units import Length, AMOUNT_UNIT

CONCRETE_INGREDIENT = TypeVar("CONCRETE_INGREDIENT", bound=Ingredient)


class Utensil(ABC):
    ...


class Container(Utensil, ABC):
    def __init__(self):
        self.contents = set()

    def transfer_to(self, value: float, unit: AMOUNT_UNIT, container: Container):
        ...

    def add(self, *ingredients: CONCRETE_INGREDIENT):
        for each_ingredient in ingredients:
            self.contents.add(each_ingredient)

    def contents(self) -> set[CONCRETE_INGREDIENT]:
        ...

    def is_content_boiling(self) -> bool:
        ...

    def is_content_thickened(self) -> bool:
        ...

    def is_content_paste(self) -> bool:
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

    def heat(self):
        ...

    def sear(self):
        ...

    def cook(self):
        ...

    def simmer(self):
        ...

    def stir(self):
        ...

    def fold(self):
        ...
