from dataclasses import dataclass

from src.utensils import ServingContainer


@dataclass
class Meal:
    container: ServingContainer
