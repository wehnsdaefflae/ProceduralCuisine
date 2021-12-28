from enum import Enum

from src.units import AMOUNT_UNIT, Amount


class CookingException(Exception):
    ...


class State(Enum):
    DEFAULT = 0
    DICED = 1
    LIQUID = 2
    FROZEN = 3
    MASHED = 4
    MELTED = 5
    COOKED = 6
    BURNT = 7
    CHOPPED = 8
    PEELED = 9
    WHOLE = 10
    FRESH = 11
    CRUSHED = 12
    CHOPPED_FINELY = 13
    CRUSHED_COARSELY = 14
    MOIST = 15
    SEARED = 16
    TRANSPARENT = 17

    RENDERED = MELTED


class Ingredient:
    def __init__(self, value: float, unit: AMOUNT_UNIT, state: set[State]):
        self.amount = Amount(value, unit)
        self.state = state

    def take_from(self, value: float, unit: AMOUNT_UNIT):
        if self.amount.value < value:
            raise CookingException("Cannot take away more than what is available!")

        if self.amount.unit != unit:
            raise CookingException("Incompatible units!")

        self.amount.value -= value
        return Ingredient(value, self.amount.unit, self.state.copy())
