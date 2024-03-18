-- Localization section --
CREATE TABLE localization (
    localization_id INTEGER PRIMARY KEY AUTOINCREMENT,
    position TEXT NOT NULL, --"LOC_..."
    language_code TEXT DEFAULT 'EN_us', --'EN_us" for us english, "FR_fr" for french, "IT_it" for italian, "ES_mx" for mexican spanish etc.
    text_value TEXT NOT NULL -- The value itself
);

-- Colors --
CREATE TABLE color ( --
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    R INTEGER NOT NULL,
    G INTEGER NOT NULL,
    B INTEGER NOT NULL
);

-- Circuit section --
CREATE TABLE circuit ( -- one of the place where we can race.
    circuit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    circuit_name TEXT NOT NULL UNIQUE, --  the name of the circuit
    nb_laps INTEGER NOT NULL, -- the number of laps during the race.
    lap_length INTEGER NOT NULL, -- [m] The length in meter of the lap.
    zoom_level FLOAT NOT NULL, -- [] The level of zoom done when zooming on the cars
    temperature INTEGER NOT NULL, -- 1 for colder circuits, 3 for hotter circuits
    humidity INTEGER NOT NULL, -- 1 for humid circuits, 3 for extra dry circuits
    wind INTEGER NOT NULL, -- 1 for no wind circuits, 3 for windy circuits.
    path_keyword TEXT NOT NULL UNIQUE -- the path to find the images and the meta-data of the circuit.
);

CREATE TABLE pit_position (
    pit_position_id INTEGER PRIMARY KEY AUTOINCREMENT,
    circuit_id INTEGER NOT NULL,
    pit_number INTEGER NOT NULL,
    abscisse FLOAT NOT NULL,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    alpha FLOAT NOT NULL,
    FOREIGN KEY (circuit_id) REFERENCES circuit(circuit_id)
);

CREATE TABLE grid_position (
    grid_position_id INTEGER PRIMARY KEY AUTOINCREMENT,
    circuit_id INTEGER NOT NULL,
    grid_number INTEGER NOT NULL,
    abscisse FLOAT NOT NULL,
    x FLOAT NOT NULL,
    y FLOAT NOT NULL,
    alpha FLOAT NOT NULL,
    FOREIGN KEY (circuit_id) REFERENCES circuit(circuit_id)
);


CREATE TABLE sector_type ( -- types are: drs straight, straight, finish line straight, drs finish line straight, full speed turn, braking turn.
    sector_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sector_type_name TEXT NOT NULL, 
    sector_type_description TEXT NOT NULL
);

CREATE TABLE sector ( -- part of a circuit, can have different types
    sector_id INTEGER PRIMARY KEY AUTOINCREMENT,
    circuit_id INTEGER NOT NULL,
    sector_type_id INTEGER NOT NULL,
    rank INTEGER, -- the rank in the circuit. If the sector type is
    sector_start FLOAT NOT NULL,
    sector_end FLOAT NOT NULL,
    FOREIGN KEY (circuit_id) REFERENCES circuit(circuit_id),
    FOREIGN KEY (sector_type_id) REFERENCES sector_type(sector_type_id)
);

CREATE TABLE braking_point ( -- an abscisse where driver have to brake to pass the next turn.
    braking_point_id INTEGER PRIMARY KEY AUTOINCREMENT,
    circuit_id INTEGER NOT NULL,
    sector_id INTEGER NOT NULL,
    turning_abscisse FLOAT NOT NULL,
    velocity_ratio FLOAT NOT NULL,
    end_of_coast_abscisse FLOAT NOT NULL,
    FOREIGN KEY (circuit_id) REFERENCES circuit(circuit_id),
    FOREIGN KEY (sector_id) REFERENCES sector(sector_id)
);

CREATE TABLE trajectory_type ( -- the different types of trajectories: normal, inner, outer, error, straight_overtake1..3, pit1...12
    trajectory_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    trajectory_type_name TEXT NOT NULL, -- A one word explaination of the trajectory type
    trajectory_type_description TEXT NOT NULL -- clear and simple explaination of what is this kind of trajectory. 
);

CREATE TABLE trajectory (
    trajectory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    circuit_id INTEGER NOT NULL, -- the circuit this trajectory refers to
    sector_id INTEGER NOT NULL, -- the sector of the circuit refers to
    previous_type INTEGER NOT NULL, -- the type of the trajectory linked with this trajectory, in the previous sector
    current_type INTEGER NOT NULL, -- the type of this trajectory
    path_keypoints TEXT NOT NULL, -- the path of the key points.
    FOREIGN KEY (circuit_id) REFERENCES circuit(circuit_id),
    FOREIGN KEY (sector_id) REFERENCES sector(sector_id),
    FOREIGN KEY (previous_type) REFERENCES trajectory_type(trajectory_type_id),
    FOREIGN KEY (current_type) REFERENCES trajectory_type(trajectory_type_id)
);

-- Pawn section --
CREATE TABLE driver (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_name TEXT NOT NULL UNIQUE,
    color_id TEXT NOT NULL, -- reprensentation of the driver.
    mass INTEGER NOT NULL, -- [kg] mass of the driver.
    pace INTEGER NOT NULL, -- the more pace the less error
    overtaking INTEGER NOT NULL, -- the more overtaking the easiest it is to overtake
    defense INTEGER NOT NULL, -- the more defense the hardest it is to be over taken
    qualifying INTEGER NOT NULL, -- the more the faster in qualifying
    starting INTEGER NOT NULL, -- the more the faster at start
    tyre_management INTEGER NOT NULL, -- the more the longer last the tyres
    price INTEGER NOT NULL, -- the price of the driver in the menu.
    experience INTEGER NOT NULL, -- the more the more efficient it is to upgrade the car between two races
    under_over_steering_trait INTEGER NOT NULL, -- 1,2,3,4,5, match the chassis of the car
    stability_trait INTEGER NOT NULL, -- 1,2,3,4,5, match the front wing of the car
    complexity_trait INTEGER NOT NULL, -- 1,2,3,4,5, match the steering wheel of the car
    hardness_trait INTEGER NOT NULL, -- 1,2,3,4,5, match the brakes of the car
    FOREIGN KEY (color_id) REFERENCES color(color_id)
);

CREATE TABLE engineer (
    engineer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    engineer_name TEXT NOT NULL UNIQUE,
    color_id INTEGER NOT NULL UNIQUE, -- linked to the team color
    price INTEGER NOT NULL,
    aerodynamics INTEGER NOT NULL, -- front and rear wing, 1 to 5
    electronics INTEGER NOT NULL, -- steering wheel
    thermodynamics INTEGER NOT NULL, -- brakes
    mechanics INTEGER NOT NULL, -- chassis
    negotiation INTEGER NOT NULL, -- price of everything else are reduced
    management INTEGER NOT NULL, -- time to evolve each part
    FOREIGN KEY (color_id) REFERENCES color(color_id)
);

-- Car section --
CREATE TABLE tyre_type (
    tyre_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tyre_type_name TEXT NOT NULL UNIQUE,
    degradation_coeff FLOAT NOT NULL, -- [state/s]
    clean_perfo_coeff FLOAT NOT NULL,
    perfo_drop_state FLOAT NOT NULL,
    zero_perfo_coeff FLOAT NOT NULL,
    perfo_at_drop FLOAT NOT NULL
);

CREATE TABLE front_wing ( -- many possibilities, unlocked with time.
    front_wing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    front_wing_name TEXT NOT NULL UNIQUE,
    perfo INTEGER NOT NULL, -- 1,2,3,4
    stability INTEGER, -- 1,2,3,4,5, match the stability criterion of the drivers.
    ancestor1 INTEGER,
    ancestor2 INTEGER,
    FOREIGN KEY (ancestor1) REFERENCES front_wing(fronr_wing_id),
    FOREIGN KEY (ancestor2) REFERENCES front_wing(fronr_wing_id)
);

CREATE TABLE steering_wheel (
    steering_wheel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    steering_wheel_name TEXT NOT NULL UNIQUE,
    perfo INTEGER NOT NULL, -- 1,2,3,4
    complexity INTEGER, -- 1,2,3,4,5 match the complexity critetion of the drivers
    ancestor1 INTEGER,
    ancestor2 INTEGER,
    FOREIGN KEY (ancestor1) REFERENCES steering_wheel(steering_wheel_id),
    FOREIGN KEY (ancestor2) REFERENCES steering_wheel(steering_wheel_id)
);

CREATE TABLE chassis (
    chassis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chassis_name TEXT NOT NULL UNIQUE,
    perfo INTEGER NOT NULL, -- 1,2,3,4
    under_over_steering INTEGER, -- 1,2,3,4,5, match tge under/over steering criterion of the drivers.
    ancestor1 INTEGER,
    ancestor2 INTEGER,
    FOREIGN KEY (ancestor1) REFERENCES chassis(chassis_id),
    FOREIGN KEY (ancestor2) REFERENCES chassis(chassis_id)
);

CREATE TABLE brakes (
    brakes_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brakes_name TEXT NOT NULL UNIQUE,
    perfo INTEGER NOT NULL, -- 1,2,3,4
    hardness INTEGER NOT NULL, -- 1,2,3,4,5, match the hardness criterion of the drivers
    ancestor1 INTEGER,
    ancestor2 INTEGER,
    FOREIGN KEY (ancestor1) REFERENCES brakes(brakes_id),
    FOREIGN KEY (ancestor2) REFERENCES brakes(brakes_id)
);

CREATE TABLE rear_wing (
    rear_wing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rear_wing_name TEXT NOT NULL UNIQUE,
    perfo INTEGER NOT NULL,
    drs_efficiency INTEGER NOT NULL,
    ancestor1 INTEGER,
    ancestor2 INTEGER,
    FOREIGN KEY (ancestor1) REFERENCES rear_wing(rear_wing_id),
    FOREIGN KEY (ancestor2) REFERENCES rear_wing(rear_wing_id)
);

CREATE TABLE engine ( -- only 7 possibilites, unlocked with money
    engine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    engine_name TEXT NOT NULL,
    power INTEGER NOT NULL, -- 1,2,3,4,5,6,7
    price INTEGER NOT NULL
);

-- Player section --
CREATE TABLE ai (
    ai_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ai_name TEXT NOT NULL UNIQUE,
    pref_engineer INTEGER,
    pref_driver1 INTEGER,
    pref_driver2 INTEGER,
    pref_driver3 INTEGER,
    malus_trait INTEGER, --1 -> 1st, 2 -> 1st driver, 3 -> 2nd driver, 4 -> driver1, 5 -> driver2, 6 -> balanced
    bonus_trait INTEGER, --1 -> balanced, 2-> 1st driver, 3-> 2nd driver, 4 -> driver1, 5 -> driver2
    card_playing INTEGER, --1 -> when full, --2 when just got, --3 random
    FOREIGN KEY (pref_driver1) REFERENCES driver(driver_id),
    FOREIGN KEY (pref_driver2) REFERENCES driver(driver_id),
    FOREIGN KEY (pref_driver3) REFERENCES driver(driver_id),
    FOREIGN KEY (pref_engineer) REFERENCES engineer(engineer_id)
);

CREATE TABLE player (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL UNIQUE,
    is_ai BOOLEAN DEFAULT FALSE,
    ai_id INTEGER DEFAULT NULL,
    FOREIGN KEY (ai_id) REFERENCES ai(ai_id)
);

-- Card section --
CREATE TABLE card_type (
    card_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_type_name TEXT NOT NULL UNIQUE,
    card_type_description TEXT NOT NULL
);

CREATE TABLE effect (
    effect_id INTEGER PRIMARY KEY AUTOINCREMENT,
    effect_name TEXT NOT NULL UNIQUE,
    effect_target INTEGER NOT NULL, -- 1: pawn, 2: player, 3: circuit
    effect_description TEXT NOT NULL
);

CREATE TABLE card (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_name TEXT NOT NULL UNIQUE,
    card_type INTEGER NOT NULL, -- 1 for bonus, 2 for neutral, 3 for malus
    color_id INTEGER NOT NULL,
    FOREIGN KEY (color_id) REFERENCES color(color_id)
);

CREATE TABLE card_effect (
    card_id INTEGER NOT NULL,
    effect_id INTEGER NOT NULL,
    duration FLOAT,
    power FLOAT,
    FOREIGN KEY (card_id) REFERENCES card(card_id),
    FOREIGN KEY (effect_id) REFERENCES effect(effect_id)
);

-- Race section --
CREATE TABLE race (
    race_id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    circuit_id INTEGER,
    FOREIGN KEY (circuit_id) REFERENCES circuit(circuit_id)
);

CREATE TABLE race_result_pawn (
    race_id INTEGER NOT NULL,
    rank INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    driver_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL, -- <=> color id
    qualifying_time INTEGER NOT NULL, -- [ms]
    qualifying_rank INTEGER NOT NULL,
    best_time INTEGER NOT NULL, -- [ms]
    race_time INTEGER NOT NULL, -- [ms]
    gap_to_first INTEGER NOT NULL, -- [ms]
    nb_pits INTEGER NOT NULL, -- number of pits of the driver
    nb_bonus_received INTEGER,
    nb_malus_received INTEGER,
    engine_state FLOAT, -- car parts states at the end of the race.
    front_wing_state FLOAT,
    rear_wing_state FLOAT,
    brakes_state FLOAT,
    stearing_wheel_state FLOAT,
    chassis_state FLOAT,
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    FOREIGN KEY (driver_id) REFERENCES driver(driver_id),
    FOREIGN KEY (team_id) REFERENCES color(color_id)
);

CREATE TABLE race_result_player (
    race_id INTEGER NOT NULL,
    rank INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    points INTEGER NOT NULL,
    front_wing_id INTEGER, -- car stats
    rear_wing_id INTEGER,
    brakes_id INTEGER,
    stearing_wheel_id INTEGER,
    chassis_id INTEGER,
    engine_id INTEGER,
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    FOREIGN KEY (engine_id) REFERENCES engine(engine_id),
    FOREIGN KEY (front_wing_id) REFERENCES front_wing(front_wing_id),
    FOREIGN KEY (rear_wing_id) REFERENCES rear_wing_id(rear_wing_id),
    FOREIGN KEY (stearing_wheel_id) REFERENCES stearing_wheel(stearing_wheel_id),
    FOREIGN KEY (brakes_id) REFERENCES brakes(brakes_id),
    FOREIGN KEY (chassis_id) REFERENCES chassis(chassis_id)
);

-- Championship section --
CREATE TABLE point_awards (
    point_awards_id INTEGER PRIMARY KEY AUTOINCREMENT,
    point_awards_name TEXT NOT NULL UNIQUE,
    pole_points INTEGER, -- the number of points given to the poleman
    pole_points_condition INTEGER, -- the maximum rank the driver needs to finish to be awarded the pole points (included).
    best_lap_points INTEGER, -- the number of points given to the best lapper
    best_lap_points_condition INTEGER,
    max_overtaking_points INTEGER, -- the number of points given to the best overtaker
    max_overtaking_points_condition INTEGER,
    dnf_can_score BOOLEAN,
    p1 INTEGER NOT NULL, -- the number of points given to the winner
    p2 INTEGER NOT NULL, -- the number of points given to the second 
    p3 INTEGER NOT NULL, -- and so on
    p4 INTEGER NOT NULL,
    p5 INTEGER,
    p6 INTEGER,
    p7 INTEGER,
    p8 INTEGER,
    p9 INTEGER,
    p10 INTEGER,
    p11 INTEGER,
    p12 INTEGER,
    p13 INTEGER,
    p14 INTEGER,
    p15 INTEGER,
    p16 INTEGER,
    p17 INTEGER,
    p18 INTEGER,
    p19 INTEGER,
    p20 INTEGER,
    p21 INTEGER,
    p22 INTEGER,
    p23 INTEGER,
    p24 INTEGER
);
CREATE TABLE championship (
    championship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    championship_name TEXT NOT NULL UNIQUE,
    point_awards_id INTEGER NOT NULL,
    FOREIGN KEY (point_awards_id) REFERENCES point_awards(point_award) 
);

CREATE TABLE championship_race (
    championship_id INTEGER NOT NULL,
    race_id INTEGER NOT NULL,
    FOREIGN KEY (championship_id) REFERENCES championship(championship_id),
    FOREIGN KEY (race_id) REFERENCES race(race_id)
);

-- Preset section --
CREATE TABLE preset (
    preset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    creator_id INTEGER NOT NULL,
    preset_name TEXT NOT NULL UNIQUE,
    creation_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    engineer_id INTEGER NOT NULL,
    driver1_id INTEGER NOT NULL,
    driver2_id INTEGER NOT NULL,
    engine_id INTEGER NOT NULL,
    front_wing_id INTEGER NOT NULL,
    rear_wing_id INTEGER NOT NULL,
    steering_wheel_id INTEGER NOT NULL,
    brakes_id INTEGER NOT NULL,
    chassis_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES player(player_id),
    FOREIGN KEY (engineer_id) REFERENCES engineer(engineer_id),
    FOREIGN KEY (driver1_id) REFERENCES driver(driver_id),
    FOREIGN KEY (driver2_id) REFERENCES driver(driver_id),
    FOREIGN KEY (engine_id) REFERENCES engine(engine_id),
    FOREIGN KEY (front_wing_id) REFERENCES front_wing(front_wing_id),
    FOREIGN KEY (steering_wheel_id) REFERENCES steering_wheel(steering_wheel_id),
    FOREIGN KEY (rear_wing_id) REFERENCES rear_wing(rear_wing_id),
    FOREIGN KEY (brakes_id) REFERENCES brakes(brakes_id),
    FOREIGN KEY (chassis_id) REFERENCES chassis(chassis_id)
);

