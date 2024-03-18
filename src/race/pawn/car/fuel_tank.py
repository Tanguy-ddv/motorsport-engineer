"""The fuel tank of the car store the fuel for the race."""

from utils.constant import FUEL_TANK_MAX_MASS, FUEL_CONSO_PER_SEC, FPS, OFFENSIVE, DEFENSIVE, NEUTRAL
from pawn.car.error import CarError

class FuelTank:

    def __init__(self, mass) -> None:
        if mass > FUEL_TANK_MAX_MASS:
            raise CarError("The fuel level of the car is too high.")
        self.mass = mass

    def consume_fuel(self, strategy) -> None:
        """
        Consume the fuel of the car.
        
        strategy: must be OFFENSIVE, NEUTRAL or DEFENSIVE: the driver current strategy
        """
        if not strategy in [OFFENSIVE, NEUTRAL, DEFENSIVE]:
            raise CarError(f'Unknown strategy: {strategy}')
        self.mass -= FUEL_CONSO_PER_SEC[strategy]/FPS