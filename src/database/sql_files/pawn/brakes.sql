-- brakes have material names.
INSERT INTO brakes (brakes_name, perfo, hardness, ancestor1, ancestor2) VALUES
("Rock"     , 1, 3, NULL, NULL),
("Iron"     , 2, 2, 1, NULL), --2
("Copper"   , 2, 4, 1, NULL), --3
("Silver"   , 3, 1, 2, NULL), --4
("Steel"    , 3, 2, 2, NULL), --5
("Nickel"   , 3, 4, 3, NULL), --6
("Lead"     , 3, 5, 3, NULL), --7
("Platinium", 4, 1, 4, NULL),
("Paladium" , 4, 2, 4, 5),
("Aluminum" , 4, 3, 5, 6),
("Diamond"  , 4, 4, 6, 7),
("Carbon"   , 4, 5, 7, NULL)