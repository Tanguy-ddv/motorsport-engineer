-- steering wheels have programming languages names.
INSERT INTO steering_wheel (steering_wheel_name, perfo, complexity, ancestor1, ancestor2) VALUES
("Python"    , 1, 3, NULL, NULL),
("Java"      , 2, 2, 1, NULL), --2
("Ruby"      , 2, 4, 1, NULL), --3
("SQL"       , 3, 1, 2, NULL), --4
("Mongo"     , 3, 2, 2, NULL), --5
("Prolog"    , 3, 4, 3, NULL), --6
("Fortran"   , 3, 5, 3, NULL), --7
("Lua"       , 4, 1, 4, NULL),
("Javascript", 4, 2, 4, 5),
("Matlab"    , 4, 3, 5, 6),
("Rust"      , 4, 4, 6, 7),
("Swift"     , 4, 5, 7, NULL)