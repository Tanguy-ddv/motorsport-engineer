INSERT INTO sector_type (sector_type_name, sector_type_description) VALUES
("Straight with DRS", "A straight where the DRS is available, must be followed by a turn with INNER/OUTER trajectories."), --1
("Straight without DRS", "The start of a DRS straight before the line or a small straight without DRS between two turns, or a full speed turn."), --2
("Pit stop", "The pit lane."), --3
("Turn", "A turn where cars have to brake and there might be an error and an outer/inner trajectory."), --4
("Grid", "A grid that start at the end and finish at the beginning of the circuit. Can be only 1 per circuit") --5