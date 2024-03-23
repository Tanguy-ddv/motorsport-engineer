"""The pawn is one of the main component of the game. Each player has two pawns. Each pawn is one driver and one car."""

from race.circuit.weather import Weather
from race.pawn.car import Car
from race.pawn.driver.driver import Driver
from utils.constant import EMPTY_CAR_MASS, FPS, G, MU_C

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
        self.max_velocity = (self.car.get_engine_force() - self.mass*MU_C*G)*self.car.get_fluid_friction_coefficient()/self.mass**2
        self.abscisse = 0 # Need to change later when the circuit is defined.
        self.ranking = None # Need to define later when the qualification process is defined.
        self.velocity = 0 # At first, the car is not moving.

    def __accelerate(self):
        """Accelerate the car."""
        # Change the car velocity
        engine_force = self.car.get_engine_force()
        air_friction_coeff = self.car.get_fluid_friction_coefficient()
        ground_friction_force = self.mass*MU_C*G
        acceleration = (engine_force - air_friction_coeff*self.velocity - ground_friction_force)/self.mass
        self.velocity_max = (engine_force-ground_friction_force)*air_friction_coeff/self.mass**2
        self.velocity += acceleration*FPS
        # Degrade the tyre and the engine
        self.car.tyres.degrade(1 - self.driver.skills.tyre_management/10)
        self.car.engine.degrade()

    def __brake(self):
        """Brake the car."""
        # Change the car velocity
        braking_force = self.car.get_braking_force()
        air_friction_coeff = self.car.get_fluid_friction_coefficient()
        ground_friction_force = self.mass*MU_C*G
        acceleration = ( - braking_force - air_friction_coeff*self.velocity - ground_friction_force)/self.mass
        self.velocity += acceleration*FPS
        # Degrade the tyre and the brakes
        self.car.tyres.degrade(1 - self.driver.skills.tyre_management/10)
        self.car.brakes.degrade()
    
    def __coast(self):
        """Don't accelerate neither brake."""
        # Change the car velocity
        air_friction_coeff = self.car.get_fluid_friction_coefficient()
        ground_friction_force = self.mass*MU_C*G
        acceleration = ( - air_friction_coeff*self.velocity - ground_friction_force)/self.mass
        self.velocity += acceleration*FPS
        # Degrade the tyre and the brakes
        self.car.tyres.degrade(1 - self.driver.skills.tyre_management/10)

    