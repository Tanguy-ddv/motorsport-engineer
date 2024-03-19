"""The circuit class stores every data of the circuit during a race."""

from database import DBManager
from circuit.weather import Weather
from circuit.sector import GridSector, TurnSector, StraightSector, DRSStraightSector, PitLaneSector
from circuit.trajectory import Trajectory
from circuit.braking_point import BrakingPoint

class Circuit:
    """The circuit class stores every data of the circuit during a race."""

    def __init__(self, id_):
        """Create a circuit with its id."""
        data = DBManager.get_data_by_id(id_, 'circuit')
        self.config = {'circuit': data['circuit_id']}
        self.weather = Weather(data['humidity'], data['temperature'], data['wind'])
        self.lap_length = data['lap_length']
        # Create the trajectories

        trajectories = [Trajectory(
                trajectory_data['previous_type'],
                trajectory_data['current_type'],
                trajectory_data['trajectory_path'],
                trajectory_data['sector_id']
            ) for trajectory_data in DBManager.get_collection_joined_by_id(id_, 'trajectory', 'circuit')]

        # Create the sectors.
        self.sectors = []
        sectors_data = DBManager.get_collection_joined_by_id(id_, 'sector', 'circuit')
        sectors_data.sort(key= lambda x: x['rank'])

        for sector_data in sectors_data:
            type_id = sector_data['sector_type_id']
            this_sector_trajectories = [trajectory for trajectory in trajectories if trajectory.sector_id == sector_data['sector_id']]

            if type_id == 3:
                # The pite lane.
                self.pit_lane_sector = PitLaneSector(sector_data['sector_start'], sector_data['sector_end'], id_, this_sector_trajectories)

            if type_id == 5:
                # The grid
                self.gird_sector = GridSector(sector_data['sector_start'], sector_data['sector_end'], id_, this_sector_trajectories)

            if type_id == 1:
                # A DRS straght
                self.sectors.append(DRSStraightSector(sector_data['sector_start'], sector_data['sector_end'], this_sector_trajectories))
            
            if type_id == 2:
                # A straight without DRS
                self.sectors.append(StraightSector(sector_data['sector_start'], sector_data['sector_end'], this_sector_trajectories))
            
            if type_id == 4:
                # A turn
                self.sectors.append(TurnSector(sector_data['sector_start'], sector_data['sector_end'], this_sector_trajectories))

        # Braking points
        
        self.braking_points = [
            BrakingPoint(
                data_braking_point['turning_abscisse'], 
                data_braking_point['end_coast_abscisse'],
                data_braking_point['velocity_ratio'])
            for data_braking_point in DBManager.get_collection_joined_by_id(id_, 'braking_point', 'circuit')]