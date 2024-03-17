"""Game constants"""


# Game constants
FPS = 30 # [Hz]
BEST_2KM_TIME = 20 # [s/2km] The expected time to do 2km at full speed with the best specs.
_BEST_MAX_VELOCITY = 1/BEST_2KM_TIME*2000 # [m/s] The max speed of the car with the best specs.

# Physics constants

## Car physics constants

### Tyre

PERFO_COEFF_PUNCTURE = 0.4 # [perfo]

### Engine

ENGINE_MIN_PERFO = 0.70 # [perfo]
ENGINE_MAX_PERFO = 0.95 # [perfo]
ENGINE_DROP = 0.15 # [state]
ENGINE_PERFO_AT_DROP = 0.85 # [perfo]

ENGINE_DEGRADATION = 0.8/(BEST_2KM_TIME*20*4) # [state/s]

### Chassis

CHASSIS_MIN_PERFO = 0.2 # [state]
CHASSIS_MAX_PERFO = 1 # [perfo]
CHASSIS_DROP = 0.2 # [state]
CHASSIS_PERFO_AT_DROP = 0.6 # [perfo]