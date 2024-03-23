"""The fuel tank of the car store the fuel for the race."""

from utils.constant import FUEL_TANK_MAX_MASS, FUEL_CONSO_PER_SEC, FPS
from race.pawn.car.error import CarError
from typing import Literal

class FuelTank:

    def __init__(self, mass) -> None:
        if mass > FUEL_TANK_MAX_MASS:
            raise CarError("The fuel level of the car is too high.")
        self.mass = mass

    def consume_fuel(self, strategy: Literal['offensive','neutral','defensive']) -> None:
        """
        Consume the fuel of the car.
        
        strategy: must be OFFENSIVE, NEUTRAL or DEFENSIVE: the driver current strategy
        """
        self.mass -= FUEL_CONSO_PER_SEC[strategy]/FPS
    
    def refuel(self, refuel_amount):
        """
        Refuel the fuel tank.
        
        refuel_amount: the mass of fuel to put in the tank.
        """
        self.mass += refuel_amount
        self.mass = min(self.mass, FUEL_TANK_MAX_MASS)