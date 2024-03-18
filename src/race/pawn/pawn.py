"""The pawn is one of the main component of the game. Each player has two pawns. Each pawn is one driver and one car."""

from circuit.weather import Weather
from pawn.car import Car
from pawn.driver.driver import Driver
from utils.constant import EMPTY_CAR_MASS

class Pawn:

    def __init__(
            self,
            front_wing_id: int,
            rear_wing_id: int,
            chassis_id: int,
            engine_id: int,
            steering_wheel_id: int,
            brakes_id: int,
            tyre_type: str | int,
            fuel_mass: int,
            weather: Weather,
            driver_id: int,
            engine_state=1,
        ) -> None:
        self.car = Car(
            front_wing_id,
            rear_wing_id,
            chassis_id,
            engine_id,
            steering_wheel_id,
            brakes_id,
            tyre_type,
            fuel_mass,
            weather,
            engine_state,
        )
        self.driver = Driver(driver_id)
        self.car.update_perfo_with_driver_trait(
            self.driver.traits.under_over_steering,
            self.driver.traits.hardness,
            self.driver.traits.complexity,
            self.driver.traits.stability
        )
        self.config = self.car.config + {'driver' : driver_id}
        
        self.mass = self.driver.mass + self.car.fuel_tank.mass + EMPTY_CAR_MASS
        