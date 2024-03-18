# Game physics

## Car mouvement

The mass of the car is represented by $m$ (in kg). It is the sum of the car, the fuel and the driver masses.

The car position is represented by an abscisse $x$ (in meters), it represent the distance from the first crossing of the start/finish line in the race. The initial $x$ at the start of the race is a negative value.

The car texture is then placed on the circuit using trajectories. A trajectory is a function $[0,1] \rightarrow \mathbb{R}^2 \times [-\pi, \pi]$ taking a reduced abscisse $(x \mod C_{\Delta})/C_{\Delta}$ where $C_\Delta$ is the length of the circuit (in meter).

The car velocity is $v = \frac{dx}{dt}$ and the car acceleration is $a = \frac{dv}{dt} = \frac{d^2x}{dt^2}$.

During its movement, the car undergo a fluid friction force with the air $F_f$ and a solid friction force with the ground $F_g$.

### Acceleration

During an acceleration, the engine energy that is transmitted to the ground by the wheels, modelized by a force $F_e$. This force depends on the engine performance and state, the weather and the tyres (type and state).

### Braking

During a braking, the brakes apply a negative force $-F_b$ on the car. This force depends on the weather, the tyre type and state, and the brake performance and state.

### Movement equations

By appliying the second law of Newton, we have the following equations:

When accelerating:

$$
am = F_e - F_f - F_g
$$

When braking:

$$
am = -F_b - F_f - F_g
$$

### Fluid friction with the air

The fluid friciton force with the air is defined by:

$$
F_f = f_fv
$$

where $f_f$ (kg/s) is a coefficient that depends on 3 other coefficients:

$$
f_f = f_{f,front} + f_{f, rear} - f_{f, DRS}
$$

with $f_{f,DRS} = 0$ when the car have not the DRS activated. The three composents depends on the weather and the performances of the front and rear wings

### Solid friction with the ground

The friction force with the ground is given by:

$$
F_g = mg\mu_C
$$

where $\mu_C$ is the friction coefficient tyre <-> ground.

## Forces, coefficients and car stats

All the performance coefficients will be noted $\pi_{i}$ with $i$ the car part it refers to. This coefficient depends on the performance value of the car part, the weather and the state.

### The engine force

The engine force is calculated with the following formula:

$$
F_e = \pi_t\pi_eF_{e, max}
$$

with $\pi_t$ the performance coefficient of the tyres, $\pi_e$ the performance coefficient of the engine and $F_{e,max}$ the maximum force an engine can provide.

### The turning velocity

When arriving at a braking point, the car should have the following velocity

$$
v = r\pi_C v_{max}
$$

where $r$ is the velocity ratio of the braking point, $v_{max}$ the max velocity of the car (calculated via the movement equation), and $\pi_C$ the performance coefficient of the chassis.

### The friction coefficients

The friction coefficient for the front wing is:

$$
f_{f,front} = \pi_{fw}^{-1}.f_f^0/2
$$

The friction coefficient for the rear wing is:

$$
f_{f,rear} = \pi_{rw}^{-1}.f_f^0/2
$$

The DRS friction coefficient of the rear wing is

$$
f_{f,DRS} = \pi_{DRS}.f_f^0/2
$$

with $\pi_{rw}$, $\pi_{fw}$ and $\pi_{DRS}$ the performance coefficient of the rear wing, front wing and DRS, and $f_f^0$ the minimal friction coefficient.

## Equation resolution

The acceleration equation is the following:

$$
am = F_e - f_fv- mg\mu_c

$$

with $\tau = \frac{f_f}{m}$ and $F = F_e - mg\mu_C$ then 

$$
a + v/\tau = F/m
$$

with $v(t=0) = 0$ then

$$
v(t) = \frac{F\tau}{m} \left (1-\exp(-\frac{t}{\tau}) \right )
$$

we have $v_{max} = \frac{Ff_f}{m^2}$
