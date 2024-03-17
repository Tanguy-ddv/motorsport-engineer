"""The Tyre class is made to represents the tyres of a pawn during the race."""

from dataclasses import dataclass
from typing import Literal
from circuit.weather import Weather
from database import DBManager
from utils.maths import affine2
from utils.constant import FPS

@dataclass(init=False)
class TyreType:
    """The TyreType stores the attributes of a tyre based on its type: soft, medium or hard."""

    def __init__(self, weather: Weather, type_id: int):
        data = DBManager.get_data_by_id(type_id, 'tyre_type')
        self.clean_perfo_coeff = data['clean_perfo_coeff']
        self.zero_perfo_coeff = data['zero_perfo_coeff']
        self.perfo_drop_state = data['perfo_drop_state']-0.1*(weather.humidity)
        self.perfo_at_drop = data['perfo_at_drop']-0.1*(weather.humidity)
        self.degradation_coeff = data['degradation_coeff']*(0.95+weather.temperature*0.05)

class Tyres:
    """The Tyre instances represents the pawn set of 4 tyres during a race."""

    def __init__(self, tyre_type: Literal['Hard', 'Medium', 'Soft', 1,2,3], weather: Weather) -> None:
        """Create a set of tyres."""
        self.state = 1
        if isinstance(tyre_type, str):
            tyre_type = {'Hard':1,'Medium':2,'Soft':3}[tyre_type]
        self.type = TyreType(weather, tyre_type)
        self.flat = False # True if the tyre is flat, when no more state or when flattened by a card.

    def get_perfo_coeff(self, state: float):
        """Calculate the performance coefficient of the tyre."""
        return affine2(
            x=state, 
            min_=self.type.zero_perfo_coeff,
            max_=self.type.clean_perfo_coeff,
            sep_x=self.type.perfo_drop_state, 
            sep_y=self.type.perfo_at_drop
        )

    def degrade(self, tyre_management_perfo_coeff: float):
        """Degrade the tyres."""
        self.state -= self.type.degradation_coeff/FPS*tyre_management_perfo_coeff
