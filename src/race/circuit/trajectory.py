"""A trajectory is a curved line followed by the pawn."""

import json
from utils.constant import TRAJECTORY_LENGTH

class Trajectory:
    """A trajectory is a curved line followed by the pawn."""

    def __init__(self, previous_type: str, current_type: str, path: str):
        """Create the trajectory."""
        self.previous_type = previous_type
        self.current_type = current_type
        self.__positions, self.__orientations = __open_trajectory(path)

    def position(self, s: float) -> tuple[float, float]:
        """
        Return the position x,y of the pawn.
        
        s: the abscisse between 0 and 1.
        """
        return self.__positions[int(s*TRAJECTORY_LENGTH)]

    def orientation(self, s: float) -> float:
        """
        Return the orientation alpha of the pawn.
        
        s: the abscisse between 0 and 1.
        """
        return self.__orientations[int(s*TRAJECTORY_LENGTH)]




def __open_trajectory(path: str):
    """Open a trajectory file."""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['positions'], data['orientations']