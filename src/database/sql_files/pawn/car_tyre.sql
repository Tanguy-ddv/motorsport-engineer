INSERT INTO tyre_type (tyre_type_name, degradation_coeff, clean_perfo_coeff, perfo_drop_state, zero_perfo_coeff, perfo_at_drop) VALUES
-- Hard tyre
-- Degradation=0.0035/s => 7%/(20s lap), 
-- perfo at best is 0.9
-- perfo drops at state=0.3
-- perfo when tyre is dead is 0.4
-- perfo at drop is 0.75: from 100% to 30%, tyre perfo -0.15 => 15/70 = 0.214
("Hard", 0.0035, 0.9, 0.4, 0.4, 0.75),
-- Medium tyre
-- Degradation = 10%/(20s lap) => 0.005/s
-- perfo at best is 0.94
-- perfo drops at state = 0.39
-- perfo when tyre is dead is 0.4
-- perfo at drop is 0.70: from 100% to 39%, tyre perfo -0.20 => 20/61 = 0.3
("Medium", 0.005, 0.94, 0.39, 0.4, 0.7),
-- Soft tyre
-- Degradation = 12%/(20s lap) => 0.006/s
-- perfo at best is 1
-- perfo drops at state = 0.5
-- perfo when tyre is dead is 0.4
-- perfo at drop is 0.80: from 100% to 50%, tyre perfo -0.20 => 20/50 = 0.4
("Soft", 0.005, 1, 0.5, 0.4, 0.8)
