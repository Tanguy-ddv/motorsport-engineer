Changelog
=========


(unreleased)
------------

New
~~~
- Add a clear frames function to switch phase during the game. [Tanguy
  Dugas du Villard]
- Possibility to write on the frames with a font given at the font
  creation. [Tanguy Dugas du Villard]
- Update of frames and screen to display objects and background on the
  frames. [Tanguy Dugas du Villard]
- Definition of the sound mixer and the input manager. [Tanguy Dugas du
  Villard]
- Definition of the screen of the engine, and its frames. [Tanguy Dugas
  du Villard]
- Definition of the engine. [Tanguy Dugas du Villard]
- Circuit initilization. [Tanguy Dugas du Villard]
- Definition of the sectors and the trajectories. [Tanguy Dugas du
  Villard]
- Definition of braking points and calculation of braking distances.
  [Tanguy Dugas du Villard]
- Pawn functions to accelerate, brake and coast (when you don't do
  anything after a braking point). add the end-of-coast logic. [Tanguy
  Dugas du Villard]
- Creation of the pawn class and its init method. [Tanguy Dugas du
  Villard]
- Resolution of movement equation. Implementation in the car class.
  [Tanguy Dugas du Villard]
- Creation of the car class to store every car parts and interact with
  them. [Tanguy Dugas du Villard]
- Introduction of race strategy in the driver and the fuel tank classes.
  [Tanguy Dugas du Villard]
- Introduction of fuel tank and strategy. [Tanguy Dugas du Villard]
- Driver class. [Tanguy Dugas du Villard]
- Add repair method to repair the part during the race. [Tanguy Dugas du
  Villard]
- Front wing of the car. [Tanguy Dugas du Villard]
- Creation of rear wing and its DRS. [Tanguy Dugas du Villard]
- Steering wheel class to manage the player deck. [Tanguy Dugas du
  Villard]
- Creation of brakes class to represent the brakes during a race.
  [Tanguy Dugas du Villard]
- Creation of the chassis as a cart part. Add of the CarError class (an
  Excepetion) to handle the errors with the car. [Tanguy Dugas du
  Villard]
- Engine class to represent an engine during the race. [Tanguy Dugas du
  Villard]
- Add of puncture, improvement of tyre degradation. [Tanguy Dugas du
  Villard]
- Tyres class to represent the tyres during the race. [Tanguy Dugas du
  Villard]
- Instance of the database manager is now created once and can by find
  at: database.DBManager. Improvement on DatabaseManager buy adding two
  basic select fonction and the ability to write the insert queries into
  a file. [Tanguy Dugas du Villard]
- Empty sql files relative to circuit data. [Tanguy Dugas du Villard]
- Database filling with drivers, engine and engineers. [Tanguy Dugas du
  Villard]
- First filling of the database. [Tanguy Dugas du Villard]
- Database manager created, a class to manage the data. [Tanguy Dugas du
  Villard]
- Documentation on the game physics and mechanics. [Tanguy Dugas du
  Villard]
- Update README, creation of CHANGELOG. [Tanguy Dugas du Villard]
- First architecture. [Tanguy Dugas du Villard]

Changes
~~~~~~~
- Removal of input manager. Inputs know managed with a method of the
  engine. [Tanguy Dugas du Villard]
- Modification of Braking Points to use the velocity ratio. [Tanguy
  Dugas du Villard]
- CHANGELOG update (0.0.1) [Tanguy Dugas du Villard]
- Database management moved from utils to its own folder. [Tanguy Dugas
  du Villard]

Fix
~~~
- Image display bug fixed. [Tanguy Dugas du Villard]
- Displaying bugs fixed. [Tanguy Dugas du Villard]
- Bug corrected on updates functions. [Tanguy Dugas du Villard]
- Made possible to load already zoomed images. [Tanguy Dugas du Villard]

Other
~~~~~
- Merge pull request #5 from Tanguy-ddv/in-game-circuit. [Tanguy Dugas
  du Villard]

  In game circuit
- Merge pull request #4 from Tanguy-ddv/in-race-pawn. [Tanguy Dugas du
  Villard]

  chg: remove of weather affecting cards. Undoable now with the currentà
- Merge pull request #3 from Tanguy-ddv/in-race-pawn. [Tanguy Dugas du
  Villard]

  In race pawn
- Merge pull request #2 from Tanguy-ddv/database-management. [Tanguy
  Dugas du Villard]

  Database management
- Merge pull request #1 from Tanguy-ddv/database-management. [Tanguy
  Dugas du Villard]

  Database management
- Initial commit. [Tanguy Dugas du Villard]


