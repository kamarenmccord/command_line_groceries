import sys
sys.path.insert(0, './source/')
from source.isle import *

# Dinner meals

beer_brats = ['beer brats', brats, beer, buns_brats, onion, celery]
beef_n_broc = ["beef and broccoli w/ fryed rice", corn_starch, steak, sause_soy, sugar_brown, garlic, season_ginger,
               broccoli, onion_white, rice_white, peas, carrot, eggs]
beef_bulganese = ["Beef Bulganese", beef_shreaded, carrot, onion, celery, red_wine, noodle_spagetti, beef_bouillon,
                  tomato_crushed, tomato_paste, garlic]
buritto = ['buritto', beef_ground, cheese_shreaded, salsa, sour_cream, sause_hot]
burger = ["burgers", buns_burger, beef_pattie, cheese_singles, catsup, mustard, lettus, tomato, bean_baked]
buritto_beancheese = ['bean and cheese burrito', bean_refryed, tortilla, cheese_shreaded, salsa, sause_hot]
cajin_alfredo_sausage = ["cajin alfredo sausage", mushroom, bell_peper, onion, garlic, noodle_spagetti,
                         broth_chicken, kielbasa, cheese_parmesan, cream_heavy, season_cajin]
carne_asada_tacos = ["carne asada taco", cilantro, pico_de_gallo, carne, salsa, sause_hot, tortilla_corn]
tacos_homemade = ['Tacos', oil_corn, tortilla_corn, cilantro, beef_ground, lettus, tomato, cheese_shreaded]
chicken_taquitoes = ["Chicken Taquitoes", oil_corn, tortilla_corn, chicken_breast, cheese_shreaded, season_taco]
chicken_alfredo = ["Chicken alfredo", peas, chicken_breast, sause_alfredo, noodle_spagetti]
chicken_leg_bbq = ["BBQ chicken legs", chicken_leg_seasoned, potato, potato_salad]
chicken_parmesan = ["Creamy parmesan Garlic Mushroom Chicken".title(), chicken_breast, mushroom, garlic, broth_chicken,
                    cream_heavy, cheese_parmesan, spinach, flour, butter]
chicken_lo_mein = ['chicken lo mien', noodle_stir_fry, veggi_snap_pea, sause_hoison, sause_soy, broth_chicken,
                   oil_seseme]
chicken_n_rice = ['chicken and rice', chicken_breast, rice_a_roni]
chicken_burrito = ['chicken burrito', tortilla, rice_white, guacamole, bean_black, salsa]
chicken_teriyaki = ['teriyaki chicken', chicken_breast, vinigar_white_wine, sause_soy, sugar_brown, mirin, oil_seseme,
                    garlic,
                    onion_green, broccoli]
corn_dogs = ['corn dogs', corn_dogs, fries]
chow_mein = ['Chow mein', la_choy, noodle_dry]
crunch_wrap = ['crunch wraps', tortilla, tortilla_hard, cheese_nacho, tomato, lettus, cheese_shreaded, sour_cream,
               beef_ground, season_taco]
enchilada = ["enchilada", tortilla, sause_enchilada, cheese_shreaded, chicken_breast, chilis_green, jalapeno, olive]
fajita = ["fajitas", tortilla, chicken_breast, bell_peper, onion, salsa, rice_a_roni, guacamole, sour_cream,
          cheese_shreaded]
fish_n_chips = ['fish n chips', talipa, fries]
hotdogs = ['hot dogs', hot_dogs, buns_hotdog, bean_baked]
hotdogs_chilli_cheese = ['chilli cheese hot dogs', hot_dogs, cheese_shreaded, chilli, buns_hotdog]
goulash = ['goulash', noodle_elbow, sausage, sause_tomato, onion, cheese_shreaded]
lasanga = ['lasanga', lasanga]
mac_cheese = ['mac and cheese', mac_n_cheese]
mac_n_cheese_hotdog = ['mac and cheese with hot dogs', mac_n_cheese, hot_dogs]
meat_loafv1 = ['meat loaf with bread crumb', beef_ground, bread_crumbs, eggs, sause_worcestershire, season_garlic_salt,
               season_black_peper, season_paprika, sause_bbq, onion]
meat_loafv2 = ['meat loaf with stuffing', beef_ground, dressing, sause_tomato, season_garlic_salt, season_black_peper,
               season_paprika, onion]
mexican_stuffed_shells = ["mexican stuffed shells", beef_ground, season_taco, cheese_cream, noodle_jumbo_shell, salsa,
                          sause_taco, cheese_shreaded, onion_green, sour_cream]
pad_tai = ['pad tai', noodle_stir_fry, eggs, chicken_breast, season_ginger, onion_green, peanut, bean_sprout,
           sause_hot_sar,
           oil_seseme, sugar_brown, oil_fish, shallots, rice_vinegar, sause_soy, lime_juice]
pot_pie = ['Pot pies', pot_pie]
pork_n_beans = ["pork and beans", meat_pork, bean_baked]
pork_n_potato_with_veggi = ["pork and potato with veggis", veggi_mix, potato, meat_pork]
pigs_n_blanket = ['pigs in a blanket', hot_dogs, cresant, catsup, potato]
pizza_shells_hawaiian = ["hawaiian pizza shells", noodle_jumbo_shell, sause_pizza, cheese_mozzarella, meat_ham,
                         pinapple]
pizza_shells_meats = ["meats pizza shells", noodle_jumbo_shell, sause_pizza, cheese_mozzarella, meat_peperoni,
                      beef_ground, bacon_bits]
pizza_shells_supream = ["supream pizza shells", noodle_jumbo_shell, sause_pizza, cheese_mozzarella, beef_ground,
                        meat_peperoni, meat_sausage, bell_peper, onion, mushroom, olive]
spagetti = ["spagetti", noodle_spagetti, sause_spagetti, beef_ground, onion, bell_peper]
steak_n_veggi = ["steak n veggi", steak, potato, veggi_mix, sause_steak]
stuffed_bell_pepers = ["stuffed bell pepers", bell_peper, rice_white, turkey_ground, tomato_diced, onion, season_garlic,
                       broth_chicken, sause_tomato, cheese_shreaded]
talipa_mix = ["talipa with veggis and potato", potato, veggi_mix, talipa, sause_tartar]
tempura_shrimp = ["tempura shrimp", tempura_shrimp, veggi_mix, rice_a_roni]
date_night = ["DATE NIGHT", dates_night]

# list no longer has to be updated alphabetically, but does need to be added if you want to choose the item
dinner_meal_list = [beer_brats, beef_bulganese, buritto, buritto_beancheese, beef_n_broc, carne_asada_tacos,
                    tacos_homemade, chicken_leg_bbq, chicken_taquitoes, chow_mein, chicken_alfredo, chicken_parmesan,
                    chicken_lo_mein, chicken_n_rice, chicken_burrito, chicken_teriyaki, corn_dogs, crunch_wrap,
                    enchilada, fajita, fish_n_chips, goulash, hotdogs, hotdogs_chilli_cheese, lasanga, mac_cheese,
                    meat_loafv1, meat_loafv2, mac_n_cheese_hotdog, mexican_stuffed_shells, pigs_n_blanket, pot_pie,
                    pizza_shells_hawaiian, pizza_shells_meats, pizza_shells_supream, stuffed_bell_pepers, pork_n_beans,
                    pork_n_potato_with_veggi, spagetti, burger, pad_tai, steak_n_veggi, talipa_mix, tempura_shrimp,
                    date_night]

# other items
tp = ["Toilet Paper", toliet_paper]

other_items = [tp]
