from car import Car
from random import randint


class UnreliableCar(Car):
    """Initialising UnreliableCar class using the Car class."""

    def __init__(self, name: str, fuel: int, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Driving the car if the reliability is big enough."""
        random_num = randint(0, 100)
        if random_num >= self.reliability:
            distance = 0
        driving_distance = super().drive(distance)
        return driving_distance
