"""The braking points of a circuit represent the abscisse at which must have a given velocity to pass, and so must brake before and coast after."""

from dataclasses import dataclass

@dataclass
class BrakingPoint:
    """
    The braking points of a circuit represent the abscisse at which must have a given velocity to pass,
    and so must brake before and coast after.
    """

    braking_abscisse: float # The abscisse at which the pawn must have a given velocity
    end_coast_abscisse: float # The abscisse at which the pawn can accelerate after the turn.
    velocity_ratio: float # The fraction of velocity max the pawn should have at the braking abscisse.
