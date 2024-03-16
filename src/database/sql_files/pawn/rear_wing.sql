-- rear wings have bird names.
INSERT INTO rear_wing (rear_wing_name, perfo, drs_efficiency, ancestor1, ancestor2) VALUES
("Chick"    , 1, 1, NULL, NULL),
("Parrot"   , 1, 2, 1, NULL), --2
("Duck"     , 2, 1, 1, NULL), --3
("Pigeon"   , 1, 3, 2, NULL), --4
("Pelican"  , 2, 2, 2, 3), --5
("Seagull"  , 3, 1, 3, NULL), --6
("Hawk"     , 1, 4, 4, NULL),
("Crow"     , 2, 3, 4, 5),
("Falcon"   , 3, 2, 5, 6),
("Eagle"    , 4, 1, 6, NULL)