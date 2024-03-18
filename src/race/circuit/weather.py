"""The weather class stores the data about the weather during a race."""

from dataclasses import dataclass

@dataclass
class Weather:
    """The Weather class stores the information about the weather during a race."""

    humidity: float
    temperature: float
    wind: float