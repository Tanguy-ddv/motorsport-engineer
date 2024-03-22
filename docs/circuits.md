# Circuits

The circuits are the places where the races take place.
Each circuit is characterised by:

- The weather:
  - temperature
  - humidity
  - wind
- The lap length (in meters)

## Sector

Each circuit is composed of sector, having the following characteristics:

- a start $x_0$ ($x \in [0,1]$)
- an end $x_1$ ($x_1 \in [0,1]$)
- a type:
  - Straight
  - DRS Straight
  - Turn
  - Pit lane
  - Start/Finnish Line Straight
  - DRS Start/Finnish Line Straight
- a rank in the circuit (except for pit lanes)
- a set of trajectories
- a set of braking points

## Trajectories

Each trajectory is a list of position $(x,y)$ and orientations $\alpha$. They also have a current type and a previous type. They are part of a sector They must accord continuously with another trajectory of the previous sector having as current type the previous type of this trajectory. They represent the list of position the car will have if they are following this trajectory
the types are:

- Normal: The normal trajectory followed by the car when they are alone on track.
- Inner/Outer: When one car try to overtake another in a turn, one take the inner trajectory while the other one take the outer
- Pit lane: The trajectory through the pit lane
- Pit stop 1 to 12: The trajectory of a car stopping in the pits.
- Error: The trajectory of a car doing an error in a turn
- Straight Overtake Early/Normal/Late: the trajectory followed by a car overtaking another in a straight or a DRS straight.

## Braking points

Braking points are a combinations of:

- an abscisse $x$ ($x \in [0,1]$)
- a velocity ratio $v_r$ ($v_r \in [0,1]$)
  A braking point represent an abscisse where the cars have to have a smaller velocity to pass a turn. The turning velocity is the maximum velocity of the car multiplied by the ratio, and then modified by the chassis of the car.

## Circuit list

The following circuit will be part of the first version of the game:

- Green garden: the first circuit in a green environment and continental climate
- Extra dry desert: Desertic climate
- Sunday Beach: Sunny beach with a lot of wind
- Andian Peaks: Montain Cold and humide mounains, and windy
- Aztec Jungle: Rain forest climate, hot and humid
- Capital Streets: Street circuit, small circuit, continental climate
- Toundra world: Toudra. No wind but cold climate
- Random Forest: Forest in a continental climate
- Bushy Island: Tropical Island, hot, windy and humid
- Terminal II: Airport, continental climate, windy
- Oval Raceway: Oval, continental climate
- Boat Club: Boat, in the middle of the see, small circuit on a boat. windy and humid.
