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
from utils.constant import BEST_ENGINE_FORCE, BEST_FLUID_FRICTION_COEFF, BEST_BRAKING_FORCE

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
    
    def get_engine_force(self) -> float:
        """Calculate the engine force."""
        return self.tyres.get_perfo_coeff()*self.engine.get_perfo_coeff()*BEST_ENGINE_FORCE
    
    def get_fluid_friction_coefficient(self, drs_activated=False) -> float:
        """Calculate the fluid friction coefficient."""
        f_front = BEST_FLUID_FRICTION_COEFF/self.front_wing.get_perfo_coeff()
        f_rear = BEST_FLUID_FRICTION_COEFF/self.rear_wing.get_drs_perfo_coeff()
        f_drs = BEST_FLUID_FRICTION_COEFF*self.rear_wing.get_drs_perfo_coeff()
        if drs_activated:
            return f_front + f_rear - f_drs
        return f_front + f_rear
    
    def get_braking_force(self) -> float:
        """Calculate the braking force."""
        return self.brakes.get_perfo_coeff()*BEST_BRAKING_FORCE

    def get_turning_ease(self) -> float:
        """Calculate the turning ease of the car."""
        return self.chassis.get_perfo_coeff()
    
    def get_card_number(self) -> float:
        """Calculate the number maximum of card that can be store in the driver's hands."""
        return self.steering_wheel.get_number_of_card()