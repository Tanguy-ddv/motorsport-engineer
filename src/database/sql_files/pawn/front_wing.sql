-- front wings have fish names.
INSERT INTO front_wing (front_wing_name, perfo, stability, ancestor1, ancestor2) VALUES
("Goldfish"  , 1, 3, NULL, NULL),
("Salmon"    , 2, 2, 1, NULL), --2
("Tuna"      , 2, 4, 1, NULL), --3
("Clownfish" , 3, 1, 2, NULL), --4
("Starfish"  , 3, 2, 2, NULL), --5
("Octopus"   , 3, 4, 3, NULL), --6
("Catfish"   , 3, 5, 3, NULL), --7
("Sturgeon"  , 4, 1, 4, NULL),
("Pufferfish", 4, 2, 4, 5),
("Barracuda" , 4, 3, 5, 6),
("Seahorse"  , 4, 4, 6, 7),
("Shark"     , 4, 5, 7, NULL)