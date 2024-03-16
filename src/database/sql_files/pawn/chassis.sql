-- chassis have insect names.
INSERT INTO chassis (chassis_name, perfo, under_over_steering, ancestor1, ancestor2) VALUES
("Ladybug"    , 1, 3, NULL, NULL),
("Fly"        , 2, 2, 1, NULL), --2
("Caterpillar", 2, 4, 1, NULL), --3
("Beetle"     , 3, 1, 2, NULL), --4
("Mantis"     , 3, 2, 2, NULL), --5
("Butterfly"  , 3, 4, 3, NULL), --6
("Bee"        , 3, 5, 3, NULL), --7
("Mosquito"   , 4, 1, 4, NULL),
("Wasp"       , 4, 2, 4, 5),
("Ant"        , 4, 3, 5, 6),
("Centiped"   , 4, 4, 6, 7),
("Spider"     , 4, 5, 7, NULL)