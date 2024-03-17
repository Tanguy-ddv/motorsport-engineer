"""The chassis of the car allows it to take the turns faster."""

from database import DBManager
from circuit.weather import Weather
from utils.maths import affine2
from race.pawn.car.error import CarError
from utils.constant import CHASSIS_MIN_PERFO, CHASSIS_MAX_PERFO, CHASSIS_DROP, CHASSIS_PERFO_AT_DROP

class Chassis:
    """The Chassis objects represents the chassis of the car during a race."""

    def __init__(self, id_: int, weather: Weather) -> None:
        """Create a chassis for a car."""
        data = DBManager.get_data_by_id(id_, 'chassis')
        self.perfo = (data['perfo'] + 1)*(1 - (weather.wind-1)/10)
        self.__trait = data['under_over_steering']
        self.state = 1
        self.__updated_with_driver_traits = False # Needs to be set to true

    def update_perfo_with_driver_trait(self, driver_trait: int):
        """Update the car perfo with the trait of the driver."""
        self.__updated_with_driver_traits = True
        self.perfo -= abs(self.__trait - driver_trait)/2 

    def get_perfo_coeff(self):
        """Get the turning ease of the car."""
        if not self.__updated_with_driver_traits:
            raise CarError("The chassis has not be updated with a driver trait yet")
        return affine2(
            x=self.state,
            min_ = (self.perfo-2)/20 + CHASSIS_MIN_PERFO,
            max_ = (self.perfo-2)/20 + CHASSIS_MAX_PERFO,
            sep_x = CHASSIS_DROP,
            sep_y = CHASSIS_PERFO_AT_DROP + (self.perfo-2)/20
        )