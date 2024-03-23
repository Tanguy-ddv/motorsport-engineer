"""The steering qheel allow the player to store and throw cards."""

from database import DBManager
from race.pawn.car.error import CarError
from race.circuit.weather import Weather

class SteeringWheel:
    """The SteeringWheel objects represents the deck capacity of the player."""

    def __init__(self, id_: int, weather: Weather) -> None:
        """Create a chassis for a car."""
        data = DBManager.get_data_by_id(id_, 'steering_wheel')
        self.perfo = data['perfo']
        self.__trait = data['complexity']
        self.state = 1
        self.__updated_with_driver_traits = False # Needs to be set to true

    def update_perfo_with_driver_trait(self, driver_trait: int):
        """Update the car perfo with the trait of the driver."""
        self.__updated_with_driver_traits = True
        self.perfo -= abs(self.__trait - driver_trait)/2

    def get_number_of_card(self):
        """Get the turning ease of the car."""
        if not self.__updated_with_driver_traits:
            raise CarError("The steering wheel has not be updated with a driver trait yet")
        return self.state*self.perfo + 1
    
    def degrade(self):
        """Degrade the steering wheel state when a card is thrown."""
        self.state -= 1/20
    
    def repair(self):
        """Repair the steering wheel during a pit stop."""
        self.state = 1