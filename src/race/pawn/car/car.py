"""The car represent the car of a pawn during the race."""

from typing import Literal

from race.pawn.car.front_wing import FrontWing
from race.pawn.car.rear_wing import RearWing
from race.pawn.car.engine import Engine
from race.pawn.car.chassis import Chassis
from race.pawn.car.steering_wheel import SteeringWheel
from race.pawn.car.brakes import Brakes
from race.pawn.car.fuel_tank import FuelTank
from race.pawn.car.tyres import Tyres
from circuit.weather import Weather

class Car:
    """The Car class represent the car during the race."""

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
            engine_state=1,
        ) -> None:

        self.front_wing = FrontWing(front_wing_id, weather)
        self.rear_wing = RearWing(rear_wing_id, weather)
        self.chassis = Chassis(chassis_id, weather)
        self.engine = Engine(engine_id, weather, engine_state)
        self.steering_wheel = SteeringWheel(steering_wheel_id, weather)
        self.brakes = Brakes(brakes_id, weather)
        self.tyres = Tyres(tyre_type, weather)
        self.fuel_tank = FuelTank(fuel_mass)

        self.config = {
            'front_wing_id' : front_wing_id,
            'rear_wing_id' : rear_wing_id,
            'chassis_id' : chassis_id,
            'engine_id' : engine_id,
            'steering_wheel_id' : steering_wheel_id,
            'brakes_id' : brakes_id
        }
    
    def pit_stop(
            self,
            tyre_type: Literal['hard', 'medium', 'soft', 1, 2, 3],
            refuel_amount: float,
            repair_front_wing: bool,
            repair_steering_wheel: bool,
            weather: Weather,
        ) -> None:
        """
        Update the car state with a pit stop.
        """
        self.tyres = Tyres(tyre_type, weather)
        self.fuel_tank.refuel(refuel_amount)
        if repair_front_wing:
            self.front_wing.repair()
        if repair_steering_wheel:
            self.steering_wheel.repair()

    def update_perfo_with_driver_trait(
            self,
            under_over_steering_trait: int,
            hardness_trait: int,
            complexity_trait: int,
            stability_trait: int
        ) -> None:
        """Update the perofrmance of the parts of car with the driver traits."""
        self.chassis.update_perfo_with_driver_trait(under_over_steering_trait)
        self.brakes.update_perfo_with_driver_trait(hardness_trait)
        self.steering_wheel.update_perfo_with_driver_trait(complexity_trait)
        self.front_wing.update_perfo_with_driver_trait(stability_trait)