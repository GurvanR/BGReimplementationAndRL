from abc import ABC, abstractmethod
from typing import Any, Optional, Union, List, Dict

import numpy as np
from numpy.random import randint
from random import choice, shuffle

from itertools import compress

class Game:
    pass
class Player:
    pass
class Card :
    pass
#Contains minions
class Warband:
    pass
class Minion: 
    pass

#Complex attributes classes
class Deathrattle:
    pass
class Dying_effect:
    pass
class Smn_else_dies_effect:
    pass
#Shop classes
class Play_minion_effect:
    pass
class Sell_effect:
    pass

#Complex attributes classes
class Deathrattle(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def trigger(self, warband1: Warband, warband2 :Warband, death_pos: int = None, minion: Minion = None):
        pass

class Dying_effect(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def trigger(self, warband1: Warband, warband2 :Warband, death_pos: int = None, minion: Minion = None):
        pass

class Smn_else_dies_effect(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def trigger(self, warband1: Warband, warband2 :Warband, death_pos: int = None, minion: Minion = None):
        pass

#Shop classes
class Play_minion_effect(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def trigger(self, warband1: Warband, warband2 :Warband):
        pass

class Sell_effect(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def trigger(self, warband1: Warband, warband2 :Warband):
        pass

# Elementary bricks
class Minion:

    def __init__(self, minion_config: dict[str, Any], warband: Warband = None) -> None:
        
        ## OUT OF DICT attributes
        self.already_attacked = False
        if warband is not None :
            self.warband = warband
        ##Shop attributes
        self.frozen = False

        ## IN DICT Attributes
        #Simple Attributes
        self.atk = minion_config['atk']
        self.health = minion_config['health']
        self.name = minion_config['name']
        self.minion_type = minion_config['minion_type']
        self.tier = minion_config['tier']
        self.cost = minion_config['cost']
        self.value = minion_config['value']
        self.alive = minion_config['alive']
        self.dvn_shld = minion_config['dvn_shld']
        self.taunt = minion_config['taunt']
        self.windfury = minion_config['windfury']
        self.claw = minion_config['claw']
        self.reborn = minion_config['reborn']
        self.venomous = minion_config['venomous']
        self.pos = minion_config['pos']
        self.magnetizations = minion_config['magnetizations']
        # Additional attributes specific to Sellemental:
        
        #Complex Attributes
        self.deathrattles = minion_config['deathrattles']
        self.dying_effects = minion_config['dying_effects']
        self.end_turn_effects = minion_config['end_turn_effects']
        self.is_attacked_effects = minion_config['is_attacked_effects']
        self.attacking_effects = minion_config['attacking_effects']
        self.after_attacking_effects = minion_config['after_attacking_effects']
        self.minion_summoning_effects = minion_config['minion_summoning_effects']
        self.smn_else_dies_effects = minion_config['smn_else_dies_effects']
        self.start_combat_effects = minion_config['start_combat_effects']
        
        #Recruit phase effects
        self.battlecries = minion_config['battlecries']
        self.play_minion_effects = minion_config['play_minion_effects']
        self.start_turn_effects = minion_config['start_turn_effects']
        self.sell_effects = minion_config['sell_effects']
        self.card_added_effects = minion_config['card_added_effects']
        self.magnetic = minion_config['magnetic']
        
        #Gestion des undead effects
        if warband is not None and 'Undead' in minion_config['minion_type'] :
            self.atk+=warband.eternal_counter
            self.health+=warband.eternal_counter

    @classmethod
    def from_name(cls, name: str, warband: Warband = None) -> "Minion":
        return cls(Minions_dict[name], warband)
    @classmethod

    def from_other_minion(cls, other_minion: "Minion", warband: Warband = None) -> "Minion":
        return cls(dict(
            atk=other_minion.atk,
            health=other_minion.health,
            name=other_minion.name,
            minion_type=other_minion.minion_type,
            tier=other_minion.tier,
            cost=other_minion.cost,
            value=other_minion.value,
            alive=other_minion.alive,
            dvn_shld=other_minion.dvn_shld,
            taunt=other_minion.taunt,
            windfury=other_minion.windfury,
            claw = other_minion.claw,
            reborn=other_minion.reborn,
            venomous=other_minion.venomous,
            pos=other_minion.pos,
            magnetizations=other_minion.magnetizations,
            magnetic=other_minion.magnetic,
            #Listed
            deathrattles=other_minion.deathrattles.copy(),
            dying_effects=other_minion.dying_effects.copy(),
            end_turn_effects=other_minion.end_turn_effects.copy(),
            is_attacked_effects=other_minion.is_attacked_effects.copy(),
            attacking_effects=other_minion.attacking_effects.copy(),
            after_attacking_effects=other_minion.after_attacking_effects.copy(),
            minion_summoning_effects=other_minion.minion_summoning_effects.copy(),
            smn_else_dies_effects=other_minion.smn_else_dies_effects.copy(),
            start_combat_effects=other_minion.start_combat_effects.copy(),
            battlecries=other_minion.battlecries.copy(),
            play_minion_effects=other_minion.play_minion_effects.copy(),
            start_turn_effects=other_minion.start_turn_effects.copy(),
            sell_effects=other_minion.sell_effects.copy(),
            card_added_effects=other_minion.card_added_effects.copy(),
            
        ), warband)
    
    def add_deathrattle_effect(self, effect: Deathrattle) -> None :
        self.deathrattles.append(effect)

    def show(self) -> None:
        print(self.name, self.atk, self.health)

class Warband:
    def __init__(self, minions: List[Minion] = None, name: str = 'Default Bname', eternal_counter: int = 0) -> None:

        self.minions = minions or []
        self.name = name
        self.all_zero_atk = False

        self.eternal_counter = eternal_counter

        for minion in self.minions :
            minion.warband = self
        
    @classmethod
    def from_other_band(cls, other_band: "Warband") -> "Warband":
        minions = [Minion.from_other_minion(minion) for minion in other_band.minions]
        return cls(minions, other_band.name + "copy", other_band.eternal_counter)

    def __getitem__(self, j: int) -> Minion:
        return self.minions[j]
    
    def __len__(self):
        return len(self.minions)
    
    def __iter__(self):
        return iter(self.minions)
    
    def index(self, minion: Minion):
        assert minion in self.minions, "warband index method error"
        return self.minions.index(minion)

    def pop(self, minion: Minion) -> None :
        self.minions.pop(self.index(minion))
    def remove(self, minion: Minion) -> None :
        self.minions.remove(minion)
    def append(self, minion: Minion) -> None :
        self.minions.append(minion)
    def insert(self, pos: int, minion: Minion) -> None :
        self.minions.insert(pos, minion)

    def summon(self, minion: Minion, pos: int = 0) -> None :
        if len(self) < 7 : 
            self.minions.insert(pos, minion)

    def next_fighter(self) -> Minion: 
        has_not_atacked = [minion for minion in self if not minion.already_attacked]
        if not has_not_atacked : 
            self.set_already_attacked()
            return self[0]
        return has_not_atacked[0]
    
    def set_already_attacked(self) -> None :
        have_already_attacked = [minion.already_attacked for minion in self if minion.atk > 0]
        if all(have_already_attacked):
            for minion in self :
                assert minion.already_attacked, "problem with minion already attack in fight method" 
                minion.already_attacked = False 

    def show(self) -> None:
        if len(self) == 0:
            return

        max_name_length = max(len(minion.name) for minion in self)
        line_length = max(30, max_name_length + 14)

        print("╔" + "═" * line_length + "╗")
        print("║ {:<{}} ║".format("Warband: " + self.name, line_length - 2))
        print("╠" + "═" * line_length + "╣")

        num_minions = len(self.minions)

        formatted_lines = []

        for minion in self.minions:
            formatted_line = "║ {:<{}} ║ {:<3} ║ {:<3} ║".format(
                minion.name, max_name_length, minion.atk, minion.health
            )
            formatted_lines.append(formatted_line)

        for line in formatted_lines:
            print(line)

        print("╚" + "═" * line_length + "╝")

class ShopBand:
    def __init__(self, minions: list[Minion] = None) -> None:
        self.minions = minions
    def __iter__(self):
        return iter(self.minions)
    def __len__(self):
        return len(self.minions)
    def __getitem__(self, key):
        return self.minions[key]
    def __setitem__(self, key, value):
        self.minions[key] = value
    def remove(self, minion: Minion):
        self.minions.remove(minion)
    def show(self) -> None:
        if len(self) == 0:
            return

        max_name_length = max(len(minion.name) for minion in self)
        line_length = max(30, max_name_length + 20)

        print("╔" + "═" * line_length + "╗")
        print("║ {:<{}} ║".format("Shopband: ", line_length - 2))
        print("╠" + "═" * line_length + "╣")

        num_minions = len(self.minions)

        formatted_lines = []

        for minion in self.minions:
            formatted_line = "║ {:<{}} ║ {:<3} ║ {:<3} ║ {:<6} ║".format(
                minion.name, max_name_length, minion.atk, minion.health,"Frozen : " + str(minion.frozen)
            )
            formatted_lines.append(formatted_line)
        for line in formatted_lines:
            print(line)
        print("╚" + "═" * line_length + "╝")
   
class Card(ABC) :
    def __init__(self, player) -> None:
        self.player = player
    def index(self):
        return self.player.hand.index(self) #returns the index of the card in the hand
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def show(self):
        pass

class minion_card(Card):
    def __init__(self, player, minion: Minion) -> None:
        super().__init__(player)
        self.minion = minion
    def play(self, pos: int = None):
        if len(self.player.warband) >= 7 : 
            print("Warband Full")
        else :
            if pos is None : 
                pos = int(input("At which position do you want to add this minion to your warband ? (1-7)" ))
                while pos>len(self.player.warband)+1 or pos < 0 : 
                    pos = int(input("At which position do you want to add this minion to your warband ? (1-7)\n Be careful, must be between 0 and len(warband) + 1" ))
            self.player.hand.remove(self)
            self.player.warband.insert(pos, self.minion) 
    def show(self):
        print("card {} :".format(self.index()))
        self.minion.show()

class Player:

    def __init__(self, number: int, warband: Warband, health: int = 30, armor: int = 0, hand: List[Card] = None,
                  money_setup: int = 3, tavern_tier: int = 1, game: Game = None, name: str = None) -> None:
        self.name = name
        self.number = number
        self.game = game
        self.warband = warband
        self.alive = True
        self.health = health
        self.armor = armor
        self.hand = hand or []
        self.money_setup = money_setup
        self.money = self.money_setup
        self.tavern_tier = tavern_tier

        self.next_opponent = None

        self.tier_up_cost = 5
        self.refresh_cost = 1
        self.shop_band = None
        self.frozen = False
    def linking_to_a_game(self, game: Game): #useful for intialisation
        self.game = game
    def take_damage(self, damage :int):
        if self.armor >=0 :
            if self.armor >= damage : self.armor -= damage
            else : 
                self.health -= damage - self.armor
                self.armor = 0
        else :
            self.health -= damage
    def tavern_size(self):
        tavern_size_map = {1: 3, 2:4, 3:4, 4:5, 5:5, 6:6, 7:6}
        return tavern_size_map[self.tavern_tier]
    def generate_shop_band(self, tavern_size: Optional[int] = None) -> ShopBand :
        if tavern_size is None :
            tavern_size = self.tavern_size()
        possible_minions = []
        for k in range(self.tavern_tier):
            possible_minions+= self.game.pool[k]
        
        showcase_minions = []
        for _ in range(tavern_size):
            chosen = choice(possible_minions)
            self.game.pool[Minions_dict[chosen]['tier']-1].remove(chosen) # (removing the chose minion from the game pool, -1 because tiers index begins at 0 
            showcase_minions.append(Minion.from_name(chosen)) # this appending will have to be enhanced because it is not necessarily a basic minion.

        return ShopBand(showcase_minions)
    
    def freeze(self):
        if self.frozen == True : 
            self.frozen = False
            for minion in self.shop_band :
                minion.frozen = False 
        else : 
            self.frozen = True
            for minion in self.shop_band :
                minion.frozen = True 

    def refresh(self):
        if self.money < self.refresh_cost : 
            print("Not enough money.")
        else : 
            self.money -= self.refresh_cost
            for minion in self.shop_band :
                self.game.pool_in(minion)
            self.shop_band = self.generate_shop_band()
            self.frozen = False
    
    def buy_minion(self, k: int):
        if len(self.hand) == 10 : 
            print("Hand is full.")
            return
        elif k > len(self.shop_band) :
            print("No minion to buy at this slot.")
            return
        k -=1 # allow a number between 1 and 7
        minion_to_buy = self.shop_band[k]
        if self.money < minion_to_buy.cost :
            print("Not enough money to buy this minion.")
        else : 
            self.money -= minion_to_buy.cost
            self.game.pool_out(minion_to_buy)
            self.hand.append(minion_card(self, self.shop_band[k]))
            self.shop_band.remove(minion_to_buy)
    
    def sell_minion(self, k:int):
        k-=1
        if k >= len(self.warband) :
            print("No minion to sell at this slot.")
        else :
            minion_to_sell = self.warband[k]
            self.money += minion_to_sell.value
            self.game.pool_in(minion_to_sell)
            self.warband.remove(minion_to_sell)

    def tier_up(self):
        if self.money < self.tier_up_cost :
            print("Not enough money") 
        else : 
            self.tavern_tier+=1
            self.money -= self.tier_up_cost

    def next_round(self):
        self.money_setup+=1
        if self.money_setup <=10 : self.money = self.money_setup
        else : self.money = 10
        if any([minion.frozen for minion in self.shop_band]):
            frozen_minions = [minion for minion in self.shop_band if minion.frozen]
            newtoadd_shopband = self.generate_shop_band(self.tavern_size() - len(frozen_minions))
            newtoadd_shopband.show()
            self.shop_band.minions += self.generate_shop_band(self.tavern_size() - len(frozen_minions)).minions
            self.shop_band.show()
        else : 
            self.shop_band = self.generate_shop_band()
        if self.tier_up_cost > 0 : self.tier_up_cost -=1

    def action(self):
        action_map = {0 : self.no_action, 1 : self.buy, 2 : self.sell,
                       3 : self.tier_up, 4 : self.refresh, 
                       5 : self.play_card, 6 : self.freeze}
        action_map[int(input("0 : No action, \n 1 : Buy,\n 2 : Sell,\n 3 : Tier up,\n 4 : Refresh,\n 5 : Play card,\n 6 : Freeze "))]() 

    def no_action(self):
        pass

    def buy(self):
        self.buy_minion(int(input("Which minion do you want to buy ? 1-7")))
    def sell(self):
        self.sell_minion(int(input("Which minion do you want to sell ? 1-7")))
    def play_card(self):
        if self.hand :
            self.hand[int(input("Which card do you want to play ? (0-9)"))].play()
        else : print("Hand empty, you don't have any card to play.")
    def hero_power(self):
        pass

    def HUD(self):
        print("TURN OF Player {} : {}, Health : {}, Armor : {}, Tavern Tier : {}, " 
                " Tier up cost : {}, Money : {} "
                .format(self.number, self.name, self.health, self.armor, self.tavern_tier, self.tier_up_cost, self.money))
        print("Your next opponent is Player {} : {} ".format(self.next_opponent.number, self.next_opponent.name))
        self.shop_band.show()
        self.warband.show()
        
        if self.hand :
            for card in self.hand :
                card.show()
        else : print("Hand empty")       
        
class Active_Hero_Power(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def activate(self) -> None:
        pass
class Passive_Hero_Power(ABC):
    def __init__(self) -> None:
        pass

class Timer :
    pass

class Game :
     
    def __init__(self, players: list["Player"], minion_types: list[str]) -> None:
          self.players = players
          Tiered_minions = [[name for name in Minions_dict 
                                 if any(minion_type in minion_types for minion_type in Minions_dict[name]['minion_type'])
                                 and Minions_dict[name]['tier'] == k] for k in range(1,8) ]
          self.pool = pool_creator(Tiered_minions)
          self.minions_pool = [name for sublist in Tiered_minions for name in sublist]  #Thus, all the initial names are in the pool.      
          self.dead_players = []
          self.duos_for_battle = []

          self.round = 1

    def pool_in(self, minion: Minion):
        if minion.name in self.minions_pool : # No assert here since it can happen, we just don't want add anormal minions.
            self.pool[minion.tier - 1].append(minion.name)
    def pool_out(self, minion: Minion) :
        if minion.name in self.pool[minion.tier - 1] : 
            self.pool[minion.tier - 1].remove(minion.name)
        else :
            print("A minion not in the pool have been bought") #It is ok that this will bring some more total copies if sold.
    def lobby_show(self):
        print("Round {}".format(self.round))
        print("Players alive are : ")
        print(", ".join("Player {}: {}".format(player.number, player.name) for player in self.players))
        print("\n")
    def next_opponents_selection(self):
        opponents = self.players
        if len(opponents) % 2 !=0 : opponents+= self.dead_players[-1]
        shuffle(opponents)
        duos = [opponents[i:i+2] for i in range(0, len(opponents), 2)]
        for duo in duos :
            duo[0].next_opponent = duo[1]
            duo[1].next_opponent = duo[0]
        self.duos_for_battle = duos
    def battles(self):
        for duo in self.duos_for_battle :
             print(f"Chances for player {duo[0].name} to win this fight : \n")
             fight_stats(duo[0].warband, duo[1].warband)
             print("Now happens the actual fight. \n")
             label, dmg, band1, band2 = fight(duo[0].warband, duo[1].warband) 
             if label == 1 : 
                 duo[1].take_damage(dmg)
             elif label == 2 :
                 duo[0].take_damage(dmg)
        new_dead_players = [player for player in self.players if player.health <=0]
        self.dead_players += new_dead_players
        if len(new_dead_players) > 0 :     
            self.players.remove(player for player in new_dead_players)
    
#Global fight functions 

def any_death(warband1: Warband, warband2: Warband) -> None:

    dead1, dead2 = [True], [True]
    while(dead1 or dead2):
        minions1copy, minions2copy = [], []
        death_positions1, death_positions2 = [], []
        reborned_minions1, reborned_pos1 = [], []
        reborned_minions2, reborned_pos2 = [], []

        dead1 = [minion for minion in warband1 if minion.health <=0]
        dead2 = [minion for minion in warband2 if minion.health <=0]
        for minion in dead1:
            dthpos = warband1.index(minion)
            death_positions1.append(dthpos)
            minions1copy.append(minion)
            if minion.reborn :
                reborned_minion = Minion.from_name(minion.name, warband1)
                reborned_minion.health = 1
                reborned_minion.reborn = False
                relative_slot = len(warband1) - dthpos
                reborned_pos1.append(relative_slot)
                reborned_minions1.append(reborned_minion)
            warband1.remove(minion)
        for minion in dead2:
            dthpos = warband2.index(minion)
            death_positions2.append(dthpos)
            minions2copy.append(minion)
            if minion.reborn :
                reborned_minion = Minion.from_name(minion.name, warband2)
                reborned_minion.health = 1
                reborned_minion.reborn = False
                relative_slot = len(warband2) - dthpos
                reborned_pos2.append(relative_slot)
                reborned_minions2.append(reborned_minion)
            warband2.remove(minion)

        
        for minion in minions2copy :
            for effect in minion.dying_effects:
                effect.trigger(warband2, warband1)
        for minion in minions1copy :
            for effect in minion.dying_effects:
                effect.trigger(warband1, warband2)
        for minion, death_pos in zip(minions2copy, death_positions2) :
            for effect in minion.deathrattles:
                effect.trigger(warband2, warband1, death_pos, minion)

        for minion, death_pos in zip(minions1copy, death_positions1) :
            for effect in minion.deathrattles :
                effect.trigger(warband1, warband2, death_pos, minion)

        for minion, slot in zip(reborned_minions1, reborned_pos1): 
            relative_slot =  len(warband1) - slot
            warband1.summon(minion, -relative_slot)
        for minion, slot in zip(reborned_minions2, reborned_pos2):
            relative_slot =  len(warband2) - slot
            warband2.summon(minion, -relative_slot) 

def claw_atck(minion: Minion, warband: Warband) -> None :
    pass #Code the claw effect here

def minion_atck_sub(minion1: Minion, minion2: Minion, warband1: Warband, warband2: Warband) -> None:
    atk1 = minion1.atk
    atk2 = minion2.atk
    assert (minion1.alive == True and minion2.alive == True), "cf line 662"
    assert(minion1.health > 0 and minion2.health > 0)
    #In case it has no atk, the next one has to attack
    if atk1 >=1 :
        if minion1.claw :
            claw_atck(minion1, warband2)
        else :
            minion1.already_attacked = True 

            if not minion1.dvn_shld : minion1.health -= atk2
            else : 
                minion1.dvn_shld = False
            if not minion2.dvn_shld : minion2.health -= atk1
            else : 
                minion2.dvn_shld = False

        any_death(warband1, warband2)
    else : 
            #Allows the case of a minion has 0 atk and just make the next minion attacking.
            new_idx = warband1.index(minion1)+1
            if new_idx < len(warband1):
                minion_atck( warband1[new_idx], minion2, warband1, warband2)
            else : 
                warband1.all_zero_atk = True 

def minion_atck(minion1: Minion, minion2: Minion, warband1: Warband, warband2: Warband) -> None:
        minion_atck_sub(minion1, minion2, warband1, warband2)
        if minion1 in warband1 and minion1.windfury :
            minion_atck_sub(minion1, minion2, warband1, warband2)

def stop_cond_fight(warband1: Warband, warband2: Warband) -> bool:
    length = len(warband1) >0 and len(warband2) >0
    both_zero_atk = warband1.all_zero_atk and warband2.all_zero_atk
    return length and not both_zero_atk

def band_attacking(warband1 : Warband, warband2: Warband, display): 
    
    taunt_minions = [minion for minion in warband2 if minion.taunt]
    if taunt_minions:
        fighter2 = choice(taunt_minions)
    else:
        fighter2 = choice(warband2)
    fighter1 = warband1.next_fighter() 
    if display : print(fighter1.name, "attacks", fighter2.name)
    minion_atck(fighter1, fighter2, warband1=warband1, warband2=warband2)
    warband1.set_already_attacked()

def fight(band1_for_fight: Warband, band2_for_fight: Warband, display = True):
    band1 = Warband.from_other_band(band1_for_fight)
    band2 = Warband.from_other_band(band2_for_fight)

    i = randint(2)
    while( stop_cond_fight(band1, band2) ):
        if i % 2 == 0 :
            band_attacking(band1,band2, display)
            if display : 
                print("attaque ",i)
                band1.show()
                band2.show()
        else :
            band_attacking(band2,band1, display)
            if display :
                print("attack number",i,".")
                band1.show()
                band2.show()
        i+=1
    
    band1_for_fight.eternal_counter = band1.eternal_counter
    band2_for_fight.eternal_counter = band2.eternal_counter
    if ( band1.all_zero_atk and band2.all_zero_atk ):
        return (0,0, band1, band2) # Equality
    if (len(band2) == 0): #Means that band1 won.
        if(len(band1)==0): 
            return (0,0, band1, band2) 
        winner = band1
        loser = band2
        label = 1
    else : 
        winner = band2 
        loser = band1
        label = 2
    dmg = sum([minion.tier for minion in winner])
    if display : print(f"{winner.name} won against {loser.name} and dealt {dmg} damages.")
    return label, dmg, band1, band2

#Simulation functions

def avg(numbers):
    if len(numbers) == 0:
        return 0  
    else:
        return sum(numbers) / len(numbers)
def fight_stats(band1_fight: Warband, band2_fight: Warband, n:int = 100, Q1: float = 0.1, Q3: float = 0.9):
    #Copies of 2snd degree, in order to avoid extra fight effect cumulating.
    #fight_stats takes original warbands, the snd degree of copy happens during the calling toi fight.
    T = []
    for _ in range(n):
        band1_for_fight = Warband.from_other_band(band1_fight)
        band2_for_fight = Warband.from_other_band(band2_fight)
        T.append(fight(band1_for_fight,band2_for_fight, display=False))
    win = sum([a[0] == 1 for a in T])
    dft = sum([a[0] == 2 for a in T])
    tie = n - win - dft
    win_dmg = [a[1] for a in T if a[0] == 1 ]
    dft_dmg = [a[1] for a in T if a[0] == 2 ]
    avg_win_dmg = avg(win_dmg)
    avg_dft_dmg = avg(dft_dmg)
    win_dmg.sort()
    dft_dmg.sort()
    if len(win_dmg) > 0 : 
        win_dmg_bounds = (win_dmg[int(len(win_dmg)*Q1)], win_dmg[int(len(win_dmg)*Q3)])
    else : win_dmg_bounds = [0,0]
    if len(dft_dmg) > 0 :
        dft_dmg_bounds =(dft_dmg[int(len(dft_dmg)*Q1)], dft_dmg[int(len(dft_dmg)*Q3)]) 
    else : dft_dmg_bounds = [0,0]
    labels =[win/n, dft/n, tie/n]
    damages = [win_dmg_bounds, dft_dmg_bounds, avg_win_dmg, avg_dft_dmg]
    
    print(f"Win : {100*labels[0]:.1f} % / Tie : {100*labels[2]:.1f} % / Loss : {100*labels[1]:.1f} %\n")
    print(f" Win damage : {win_dmg_bounds[0]:.1f} / avg : {avg_win_dmg:.1f} / {win_dmg_bounds[1]:.1f}\n")
    print(f" Loss damage : {dft_dmg_bounds[0]:.1f} / avg :{avg_dft_dmg:.1f} / {dft_dmg_bounds[1]:.1f}\n")
    return #labels, damages


# Other imports 
from objects_lists.BG_minions_list import Minions_dict
from objects_lists.BG_hero_list import hero_armor_map

from global_functions.BG_global_game_functions import pool_creator