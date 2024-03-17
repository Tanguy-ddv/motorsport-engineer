"""The brakes allow the car to brake before a turn."""

from database import DBManager
from utils.maths import affine2
from utils.constant import BRAKES_DEGRADATION, BRAKES_MAX_PERFO, BRAKES_PERFO_AT_DROP, BRAKES_MIN_PERFO, BRAKES_DROP, FPS
from race.pawn.car.error import CarError
from circuit.weather import Weather

class Brakes:
    """The Brakes objects represents the brakes of the car during a race."""

    def __init__(self, id_: int, weather: Weather) -> None:
        """Create thr brakes for a car."""
        data = DBManager.get_data_by_id(id_, 'brakes')
        self.perfo = (data['perfo'] + 1)*(1 - (weather.humidity-1)/10)
        self.__trait = data['hardness']
        self.state = 1
        self.__updated_with_driver_traits = False # Needs to be set to true
        self.__degradation_coeff = BRAKES_DEGRADATION*(1 + (weather.temperature-1)/10)

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
            min_ = (self.perfo-2)/20 + BRAKES_MIN_PERFO,
            max_ = (self.perfo-2)/20 + BRAKES_MAX_PERFO,
            sep_x = BRAKES_DROP,
            sep_y = BRAKES_PERFO_AT_DROP + (self.perfo-2)/20
        )
    
    def degrade(self):
        """Degrade the brakes during a braking."""
        self.state -= self.__degradation_coeff/FPS