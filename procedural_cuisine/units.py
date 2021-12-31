from dataclasses import dataclass
from enum import Enum


class Unit(Enum):
    ...


class MassUnit(Unit):
    GRAMS = 0
    POUND = 1


class VolumeUnit(Unit):
    LITERS = 0
    CUPS = 1


class ImpreciseUnit(Unit):
    TEASPOONS = 0
    TO_TASTE = 1
    BIG = 2
    SMALL = 3
    PIECES = 4
    SERVING = 5
    PINCH = 6
    ALL = 7


AMOUNT_UNIT = MassUnit | VolumeUnit | ImpreciseUnit


@dataclass
class Amount:
    value: float
    unit: AMOUNT_UNIT


class LengthUnit(Unit):
    CENTIMETERS = 0


@dataclass
class Length:
    value: float
    unit: LengthUnit
