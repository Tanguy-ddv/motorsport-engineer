"""The Front wing is the front of the car."""

from database import DBManager
from circuit.weather import Weather
from utils.maths import affine2
from race.pawn.car.error import CarError
from utils.constant import FRONT_WING_DROP, FRONT_WING_MAX_PERFO, FRONT_WING_MIN_PERFO, FRONT_WING_PERFO_AT_DROP

class FrontWing:
    """The FrontWing objects represents the front wing of the car during a race."""

    def __init__(self, id_: int, weather: Weather) -> None:
        """Create a chassis for a car."""
        data = DBManager.get_data_by_id(id_, 'chassis')
        self.perfo = (data['perfo'] + 1)*(1 - (weather.wind-1)/8)
        self.__trait = data['stability']
        self.state = 1
        self.__updated_with_driver_traits = False # Needs to be set to true

    def update_perfo_with_driver_trait(self, driver_trait: int):
        """Update the car perfo with the trait of the driver."""
        self.__updated_with_driver_traits = True
        self.perfo -= abs(self.__trait - driver_trait)/2 

    def get_perfo_coeff(self):
        """Get the performance coefficient of the front wing."""
        if not self.__updated_with_driver_traits:
            raise CarError("The rear wing has not be updated with a driver trait yet")
        return affine2(
            x=self.state,
            min_ = (self.perfo-2)/20 + FRONT_WING_MIN_PERFO,
            max_ = (self.perfo-2)/20 + FRONT_WING_MAX_PERFO,
            sep_x = FRONT_WING_DROP,
            sep_y = FRONT_WING_PERFO_AT_DROP + (self.perfo-2)/20
        )