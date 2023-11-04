from numpy.random import randint
from random import choice, sample, shuffle

from BG_primary_objects_definition import Minion, Warband, ShopBand, Player, Game, Timer
from BG_primary_objects_definition import Deathrattle

minion_types = ['Elemental', 'Demon', 'Undead', 'Dragon', 'Quilboar', 'Mech', 'Beast', 'Pirate', 'Murloc', 'Naga']

def pool_creator(tiered_minions: list[list[str]]) -> list[list[str]]:
    tiered_pool = [[] for _ in range(7)]
    for i, j in enumerate([18, 15, 13, 11, 9, 7, 7]) :
        for _ in range(j):
            tiered_pool[i]+=(tiered_minions[i])
    return tiered_pool

def hero_pool_creator(number_of_players: int):
    hero_list = heroes_list.copy()
    shuffle(hero_list)
    return [hero_list[i:i+4] for i in range(0, 4*number_of_players, 4)]
    
def game_launcher(nb_players : int = 8, time_scale: Timer = 3 ):
    #drawn_minion_types = sample(minion_types, 5)
    drawn_minion_types = ['Elemental', 'Demon', 'Undead', 'Dragon', 'Quilboar']
    drawn_minion_types.append('Neutral')
    drawn_heroes = hero_pool_creator(nb_players)
    pre_players = [Player(i+1, Warband()) for i in range(nb_players)]
    #(print("are the hands same ? ", id(pre_players[0].hand) == id(pre_players[1].hand) ))
    game = Game(pre_players, drawn_minion_types)
    for player, hero_group in zip(game.players, drawn_heroes) : 
        player.linking_to_a_game(game)
        print(hero_group)
        chosen_hero = hero_group[int(input("Player {} . Choose your Hero, 1, 2, 3 ou 4".format(player.number))) - 1]
        player.hero_power = hero_power_map[chosen_hero]
        player.name = chosen_hero
        player.warband.name = chosen_hero
        player.armor = hero_armor_map[player.name]
        player.shop_band = player.generate_shop_band() #Shop initialisation
    
    while(len(game.players) >= 2):
        game.next_opponents_selection()
        for _ in range(time_scale) :
            shuffle(game.players) 
            for player in game.players :
                game.lobby_show()
                player.HUD()
                player.action()
        game.battles()
        for player in game.players :
            player.next_round()
        game.round+=1
    print("La partie est terminée")
    game.lobby_show()

from objects_lists.BG_hero_list import hero_armor_map, heroes_list, hero_power_map