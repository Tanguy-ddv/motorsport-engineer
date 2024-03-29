"""Game constants"""


# Game constants
FPS = 30.0 # [Hz]
TRAJECTORY_LENGTH = 20000 # [] The number of points in a trajectory.

DISTANCE_DETECTION_START_DRS = 0.03 # [] The distance in proportion of the circuit, between the detection line and the starting line of the DRS.

## Geomerty constants

WIDTH, HEIGHT = 1250, 703 # The ratio needs to be 16/9 to fit the screen with black lines.
CIRCUIT_WIDTH, CIRCUIT_HEIGHT = 1151, 610

## Strategy constants

OFFENSIVE = 'offensive'
DEFENSIVE = 'defensive'
NEUTRAL = 'neutral'

## Sector types

DRS_STRAIGHT = 'DRS_straight'
STRAIGHT = 'straight'
TURN = 'turn'
PIT_LANE = 'pit_lane'
GRID = 'grid'

# Physics constants

## Car physics constants

_BEST_2KM_TIME = 20.0 # [s/2km] The expected time to do 2km at full speed with the best specs.
_BEST_MAX_VELOCITY = 1/_BEST_2KM_TIME*2000 # [m/s] The max speed of the car with the best specs.
_BEST_RACE_DURATION = _BEST_2KM_TIME*20 # [s/40km] The expected time
_ACCELERATION_TIME_CONSTANT = 2 # [s] The time needed to reach 63% of the maximum velocity

### Tyre

PERFO_COEFF_PUNCTURE = 0.4 # [perfo]

### Engine

ENGINE_MIN_PERFO = 0.70 # [perfo]
ENGINE_MAX_PERFO = 0.95 # [perfo]
ENGINE_DROP = 0.15 # [state]
ENGINE_PERFO_AT_DROP = 0.85 # [perfo]

ENGINE_DEGRADATION = 0.8/(_BEST_RACE_DURATION*4) # [state/s]

### Chassis

CHASSIS_MIN_PERFO = 0.2 # [state]
CHASSIS_MAX_PERFO = 1.0 # [perfo]
CHASSIS_DROP = 0.2 # [state]
CHASSIS_PERFO_AT_DROP = 0.6 # [perfo]

### Brakes

BRAKES_MIN_PERFO = 0.65 # [state]
BRAKES_MAX_PERFO = 0.95 # [perfo]
BRAKES_DROP = 0.98 # [state]
BRAKES_PERFO_AT_DROP = 0.92 # [perfo]

BRAKES_DEGRADATION = 1.0/750 # [state/s] The brakes last 6 brakes/lap * 42 laps * 3 s/brakes

### Rear wing

REAR_WING_MIN_PERFO = 0.45
REAR_WING_MAX_PERFO = 0.95
REAR_WING_DROP = 0.8
REAR_WING_PERFO_AT_DROP = 0.85

### Front wing

FRONT_WING_MIN_PERFO = 0.2
FRONT_WING_MAX_PERFO = 0.95
FRONT_WING_DROP = 0.4
FRONT_WING_PERFO_AT_DROP = 0.75

### Fuel tank
FUEL_TANK_MAX_MASS = 110 # [kg]
_BASIC_FUEL_CONSO_PER_SEC = 110/_BEST_RACE_DURATION # [kg/s]
FUEL_CONSO_PER_SEC = {
    OFFENSIVE : _BASIC_FUEL_CONSO_PER_SEC*1.3,
    NEUTRAL : _BASIC_FUEL_CONSO_PER_SEC,
    DEFENSIVE : _BASIC_FUEL_CONSO_PER_SEC*0.7
}

## Movement equation phyisic constants.
EMPTY_CAR_MASS = 730 # [kg]
_LIGHTER_CAR_MASS = 800 # [kg]


BEST_FLUID_FRICTION_COEFF = _LIGHTER_CAR_MASS/_ACCELERATION_TIME_CONSTANT/2
_BEST_ENGINE_FORCE_AND_GROUND_FRICTION = _BEST_MAX_VELOCITY*_LIGHTER_CAR_MASS**2/BEST_FLUID_FRICTION_COEFF
G = 9.81 # [m/s^2] the gravitational field on earth.
MU_C = _BEST_ENGINE_FORCE_AND_GROUND_FRICTION/(G*_LIGHTER_CAR_MASS)/10
BEST_ENGINE_FORCE = _BEST_ENGINE_FORCE_AND_GROUND_FRICTION - MU_C*G*_LIGHTER_CAR_MASS
BEST_BRAKING_FORCE = BEST_ENGINE_FORCE/2

# Network constants

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345