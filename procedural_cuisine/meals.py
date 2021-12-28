from dataclasses import dataclass

from procedural_cuisine.utensils import ServingContainer


@dataclass
class Meal:
    container: ServingContainer
