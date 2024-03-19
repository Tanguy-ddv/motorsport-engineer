# Trajectory, Sectors, Overtaking

## Sector

A circuit can be shattered in sectors. Except for the Pit Lane Sector and the Grid Sector, that are both present once, the other sectors all have a start abscisse and an end abscisse, the may follow each other. Each sector contains several trajectories.

## Trajectory

A trajectory is a list of $(x,y,\alpha)$. Each trajectory has a current type and a previous type. The types are used by the pawn to change trajectory. As two pawns shouldn't touch, they used the different trajectories to overtake and defend. They also use them when they make an error. A trajectory is called with a float between 0 and 1, which is the pawn_abscisse/circuit_length % 1.

## Braking Point

The braking points represents the turns of the circuit. Arriving at the braking abscisse, the pawn should have the right velocity to pass the turn. Then, the pawn coast until the end_of_coast_abscisse. Using the movement equation during a braking, we can calculate the braking distance.

$$
am = - F_b - f_fv - F_g
$$

and $v(0) = v_0$ then with $\tau = m/f_f$ and $K = (F_b + F_g)/m$

$$
v(t) = \left ( v_0 + \tau K \right ) \exp(-t/\tau) - \tau K
$$

Then, to have $v(t_1) = v_1$, the turning velocity, we have

$$
t_1 = \tau \ln \left ( \frac{v_0 + \tau K}{v_1 + \tau K} \right)
$$

so

$$
d = \int_{t=0}^{t=t_1} v(t)dt
$$

$$
d = - \tau Kt_1 + \frac{ \left ( v_0 + \tau K \right )}{\tau} \left ( 1 - \exp(-t_1/\tau) \right )
$$
