"""The rear wing make the car faster with and without DRS."""

from database import DBManager
from utils.maths import affine2
from utils.constant import REAR_WING_MIN_PERFO, REAR_WING_MAX_PERFO, REAR_WING_DROP, REAR_WING_PERFO_AT_DROP
from circuit.weather import Weather

class RearWing:
    """The RearWing objects represents the rear wing of the car during the race."""

    def __init__(self, id_: int, weather: Weather) -> None:
        """Create thr brakes for a car."""
        data = DBManager.get_data_by_id(id_, 'brakes')
        self.perfo = (data['perfo'] + 1)*(1 - (weather.wind-1)/10)
        self.drs_efficiency = (data['drs_efficiency'])
        self.state = 1

    def get_perfo_coeff(self):
        """Get the turning ease of the car."""
        return affine2(
            x=self.state,
            min_ = (self.perfo-2)/20 + REAR_WING_MIN_PERFO,
            max_ = (self.perfo-2)/20 + REAR_WING_MAX_PERFO,
            sep_x = REAR_WING_DROP,
            sep_y = REAR_WING_PERFO_AT_DROP + (self.perfo-2)/20
        )
    
    def get_drs_perfo_coeff(self):
        """Get the DRS performance coefficient."""
        if self.state >= 0.5:
            return REAR_WING_MAX_PERFO*(1+self.drs_efficiency/5)
        return 0