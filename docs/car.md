# Car

Each player create one car at the beginning of the game. The car will be able to evolve between each race

## Car composition

A car is a composed by different car parts:

### Front wing

The front wing is at the front of the car. The front wing performance will decrease the friction coefficient between the air and the car. The front wing also have a stability trait that needs to match the driver stability trait to have full performance.

The state of the FW will increase the performance.

At the start of the race, the state is 100%. The wing can be changed during a pit stop but this will make the stop last longer.

### Rear wing

The rear wing is at the rear of the car. The front wing performance will decrease the friction coefficient between the air and the car. The rear wing also have a DRS performance. The rear wing is a trade-off between frict

ion coefficient and DRS performance.

If the state of the RW is less than 50%, then the DRS can't be used.

At the start of the race, the state is 100%

### Engine

The engine is the power unit of the car. The performance of the engine will increase the force produced by the engine to accelerate the car. A bad state of the engine will reduce the performance. A really bad state will increase the probability of DNF. At the start of the race, the state is the same as the finish of the previous race. $\left \lfloor 3 \times N_{race} \right \rfloor +1$ engines can be used during the championship. Engine are designed to last 4 races. The engine is damaged everytime the driver accelerates.

### Brakes

The brakes allows the car to brake approaching a braking point. The brakes performance will increase the braking force. A car with better brakes will brake later and be able to defende and overtake more easily. Dammaged brakes will decrease the braking force. The brakes dammage itself when the driver brakes.

The brake also have a hardness trait that needs to match the driver hardness trait to get better performance.

The brake state at the start of the race is 100%

### Steering wheel

The steering wheel allows the player to have more cards in his/her hands. The steering wheel performance will increase the number of cards in the hand of the player. Each card played damage the steering wheel. A car with a completely damaged steering wheel will DNF. The steering wheel can be changed during a pit stop, but it will make the pit stop last longer. 

The state of the steering wheel at start is 100%

The steering wheel also have a complexity trait that needs to match the complexity trait of the driver to improve the performance.

### Chassis

The chassis is everything else except the tyres.

The chassis performance will increase the turning velocity. A damaged chassis will decrease its performance. 

The state of the chassis at the beginning of the race is 100%

## Pawn and Car creation

Each player have 400 $\Psi$ (money) to spend as well as 1000 h (time).

The creation of the pawn is done in 4 steps

- Choose an engineer, pay him with $\Psi$ (from 95 to 125).
- Choose an engine supplier, pay it with $\Psi$ (from 95 to 125 minus negotation bonuses).
- Choose two drivers, pay them with $\Psi$ (from 95 to 125 minus negotiation bonuses, each).
- Speed the time you have to upgrade the car:
  - The car parts needs 80 h (perfo=2), 120 h (perfo=3) and 160 h (perfo=4) to develop from a part with immediate lower perfo.
  - These times are reduces based on the engineer bonuses
  - While the time flows, the player select the evolutions by clicking on them.
  - The evolutations are represented by trees.
  - For every part except of rear wings:
    - The depth of the part in the tree is its performance, the left-right is the trait that should match the drivers traites.
    - The drivers traits for every parts is indicated.
  - For the rear wing:
    - The depth is the sum of the performance and the DRS performance.
    - The right-left is the trade-off between the two.
