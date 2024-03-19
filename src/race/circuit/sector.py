"""A sector is a part of the circuit."""

from utils.constant import DRS_STRAIGHT, STRAIGHT, TURN, PIT_LANE, GRID, DISTANCE_DETECTION_START_DRS
from database import DBManager
from .trajectory import Trajectory

class Sector:
    """Abstract layer to represent every sector."""

    def __init__(self, start, end, trajectories: list[Trajectory]):
        """Create a sector."""
        self.start = start
        self.end = end
        self.trajectories = trajectories
    
    def get_trajectory_types(self):
        """Return all the trajectory types available for this sector."""
        return set(trajectory.current_type for trajectory in self.trajectories)
    
class StraightSector(Sector):
    """Straight or full throttle turns, witout DRS."""

    def __init__(self, start, end, trajectories):
        """Create a straight sector."""
        super().__init__(start, end, trajectories)
        self.type = STRAIGHT

class DRSStraightSector(Sector):
    """A Straight where the DRS can be open."""

    def __init__(self, start, end, trajectories):
        """Create a DRS straight sector."""
        super().__init__(start, end, trajectories)
        self.detection = start - DISTANCE_DETECTION_START_DRS
        self.type = DRS_STRAIGHT
    
class TurnSector(Sector):
    """A turn where there is a braking point."""

    def __init__(self, start, end, trajectories):
        """Create a turn sector."""
        super().__init__(start, end, trajectories)
        self.type = TURN

class PitLaneSector(Sector):
    """The pit lane is unique in the circuit. It store the data about the positions of the pits."""

    def __init__(self, start, end, circuit_id, trajectories):
        """Create a pit lane sector."""
        super().__init__(start, end, trajectories)
        self.type = PIT_LANE
        # Query the DBManager to get the positions, orientations and abscisses of the pits
        data_pits = DBManager.get_collection_joined_by_id(circuit_id, 'pit_position','circuit')
        data_pits.sort(key=lambda x: x['grid_number'])
        self.pit_positions = [(data_pit['x'], data_pit['y']) for data_pit in data_pits]
        self.pit_orientations = [data_pit['alpha'] for data_pit in data_pits]
        self.pit_abscisse = [data_pit['abscisse'] for data_pit in data_pits]


class GridSector(Sector):
    """The grid sector is unique in the circuit. it store the data about the positions of the grid."""

    def __init__(self, start, end, circuit_id, trajectories):
        """Create a grid sector"""
        super().__init__(start, end, trajectories)
        self.type = GRID
        # Query the database to get the positions, orientations and absicsses of the grid
        data_grids = DBManager.get_collection_joined_by_id(circuit_id, 'grid_position','circuit')
        data_grids.sort(key=lambda x: x['grid_number'])
        self.grid_positions = [(data_grid['x'], data_grid['y']) for data_grid in data_grids]
        self.grid_orientations = [data_grid['alpha'] for data_grid in data_grids]
        self.grid_abscisse = [data_grid['abscisse'] for data_grid in data_grids]

