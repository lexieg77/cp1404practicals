from car import Car
from random import randint


class UnreliableCar(Car):
    """Initialising UnreliableCar class using the Car class."""

    def __init__(self, name: str, fuel: int, reliability: float):
        """Initialise unreliable car class"""
        super().__init__(name, fuel)
        self.reliability = reliability

