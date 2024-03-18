"""The driver class represent the driver and its characteristics during the race."""

from typing import Literal
from dataclasses import dataclass
from utils.constant import OFFENSIVE, DEFENSIVE
from database import DBManager

@dataclass
class DriverTraits:
    """The DriverTraits class stores the trait data of the driver."""

    under_over_steering: int
    complexity: int
    hardness: int
    stability: int

@dataclass
class DriverSkills:
    """The DriverStats class store the skills of the driver."""

    pace: int
    qualifying: int
    start: int
    overtaking: int
    defense: int
    tyre_management: int
    experience: int


class Driver:
    """
    The driver class represent the driver during the race.

    The driver have traits and characteristics.
    """

    def __init__(self, id_) -> None:
        """Create an instance"""
        data = DBManager.get_data_by_id(id_, 'driver')
        self.skills = DriverSkills(
            data['pace'],
            data['qualifying'],
            data['start'],
            data['overtaking'],
            data['defense'],
            data['tyre_management'],
            data['experience']
        )

        self.initial_skills = DriverSkills(
            data['pace'],
            data['qualifying'],
            data['start'],
            data['overtaking'],
            data['defense'],
            data['tyre_management']
        )

        self.traits = DriverTraits(
            data['under_over_steering_trait'],
            data['complexity_trait'],
            data['hardness_trait'],
            data['stability_trait']
        )

        self.mass = data['mass']

    def win_experience(self):
        """Win experience at the end of the race."""
        if self.initial_skills.experience < 5:
            self.initial_skills.experience += 1
            self.skills.experience += 1

    def reinit_skills(self):
        """Reinitialize the skills of the driver based on its initial skills"""
        self.skills = DriverSkills(
            self.initial_skills.pace,
            self.initial_skills.qualifying,
            self.initial_skills.start,
            self.initial_skills.overtaking,
            self.initial_skills.defense,
            self.initial_skills.tyre_management
        )
    
    def change_strategy(self, strategy: Literal['offensive','neutral','defensive']):
        """Change the driver strategy whill virtually change the driver skills."""
        self.reinit_skills()

        if strategy == OFFENSIVE:
            self.skills.tyre_management -= 1
            self.skills.pace -= 1
            self.skills.overtaking += 1
            self.skills.defense -= 1

        elif strategy == DEFENSIVE:
            self.skills.tyre_management += 1
            self.skills.pace += 1
            self.skills.overtaking -= 1
            self.skills.defense += 1