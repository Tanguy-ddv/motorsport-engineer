"""The engine is the part of the car that make it accelerate."""

from circuit.weather import Weather
from database import DBManager
from utils.constant import ENGINE_MIN_PERFO, ENGINE_MAX_PERFO, ENGINE_DROP, ENGINE_PERFO_AT_DROP, ENGINE_DEGRADATION, FPS
from utils.maths import affine2

class Engine:
    """An instance of the class Engine represents the engine of a car during a race."""

    def __init__(self, id_: int, weather: Weather, state: float=1):
        """Create the instance with the value in the database"""
        data = DBManager.get_data_by_id(id_, 'engine')
        self.power = data['power']*(1-0.1*(weather.wind + weather.humidity - 2))
        self.state = state
        self.__degradation_coeff = ENGINE_DEGRADATION*(1 + 0.08*(weather.temperature -1))

    def get_perfo_coeff(self):
        """Get the performance coefficient of the engine."""
        return affine2(
            x=self.state, 
            min_= ENGINE_MIN_PERFO + self.power/100,
            max_= ENGINE_MAX_PERFO + self.power/100,
            sep_x= ENGINE_DROP,
            sep_y= ENGINE_PERFO_AT_DROP + self.power/100
        )

    def degrade(self):
        """Degrade the engine."""
        self.state -= self.__degradation_coeff/FPS
