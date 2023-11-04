#Equivalent #from Complex_attributes import BG_deathrattles as Deathrattle Mais VScode n'auto complète pas 
#cette syntaxe par défault.
from BG_primary_objects_definition import Minion

import Complex_attributes.BG_deathrattles as Deathrattle
import Complex_attributes.BG_dying_effects as Dying_effect

import Shop_effects.BG_play_minion_effects as Play_minion_effect
import Shop_effects.BG_sell_effects as Sell_effect

#Undead
#Tier 1
Risen_Rider = dict(
    #Simple attributes :
        pos = 0,
        atk = 2, 
        health = 1, 
        name = 'Risen Rider',
        minion_type = ['Undead'],
        tier = 1,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = True,
        windfury = False,
        claw = False,
        reborn = True,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [Dying_effect.Eternal_Knight()],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)
#Tier 2
Eternal_Knight = dict(
    #Simple attributes :
        pos = 0,
        atk = 4, 
        health = 1, 
        name = 'Eternal Knight',
        minion_type = ['Undead'],
        tier = 2,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [Dying_effect.Eternal_Knight()],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)
#Tier 4
Soulsplitter = dict(
    #Simple attributes :
        pos = 0,
        atk = 4, 
        health = 2, 
        name = 'Soulsplitter',
        minion_type = ['Undead'],
        tier = 4,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = True,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [], #To fulfill

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Tier 6
Eternal_Summoner = dict(
    #Simple attributes :
        pos = 0,
        atk = 8, 
        health = 1, 
        name = 'Eternal Summoner',
        minion_type = ['Undead'],
        tier = 6,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [Deathrattle.summon(Minion(Eternal_Knight))],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)
Sister_Deathwhisper = dict(
    #Simple attributes :
        pos = 0,
        atk = 4, 
        health = 10, 
        name = 'Sister Deathwhisper',
        minion_type = ['Undead'],
        tier = 6,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [], #To fulfill
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Elemental
#Tier 2
Molten_Rock = dict(
    #Simple attributes :
        pos = 0,
        atk = 3, 
        health = 4, 
        name = 'Molten Rock',
        minion_type = ['Elemental'],
        tier = 2,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = True,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Tier 1 
Sellemental = dict(
    #Simple attributes :
        pos = 0,
        atk = 2, 
        health = 2, 
        name = 'Sellemental',
        minion_type = ['Elemental'],
        tier = 1,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)
# Neutral 

#Tier 1

#Tier 2
Spawn_of_Nzoth = dict(
    #Simple attributes :
        pos = 0,
        atk = 2, 
        health = 2, 
        name = 'Spawn of NZoth',
        minion_type = ['Neutral'],
        tier = 2,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [Deathrattle.NZoth()],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Tier 5
Leeroy_The_Reckless = dict(
    #Simple attributes :
        pos = 0,
        atk = 6, 
        health = 2, 
        name = 'Leeroy The Reckless',
        minion_type = ['Neutral'],
        tier = 5,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [], ##
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Demons
#Tier 1
#Tier 2
Backstage_Security = dict(
    #Simple attributes :
        pos = 0,
        atk = 4, 
        health = 6, 
        name = 'Backstage Security',
        minion_type = ['Demon'],
        tier = 2,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)
Soul_Rewinder = dict(
    #Simple attributes :
        pos = 0,
        atk = 2, 
        health = 1, 
        name = 'Soul Rewinder',
        minion_type = ['Demon'],
        tier = 2,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Tier 3
Legion_Overseer = dict(
    #Simple attributes :
        pos = 0,
        atk = 4, 
        health = 2, 
        name = 'Legion Overseer',
        minion_type = ['Demon'],
        tier = 3,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Dragons
#Tier 2
Low_Flier = dict(
    #Simple attributes :
        pos = 0,
        atk = 3, 
        health = 2, 
        name = 'Low-Flier',
        minion_type = ['Dragon'],
        tier = 2,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)

#Quilboars

#Tier 3
Prickly_Piper = dict(
    #Simple attributes :
        pos = 0,
        atk = 3, 
        health = 1, 
        name = 'Prickly Piper',
        minion_type = ['Quilboar'],
        tier = 2,
        alive = True,
        cost = 3,
        value = 1,
        dvn_shld = False,
        taunt = False,
        windfury = False,
        claw = False,
        reborn = False,
        venomous = False, 
        magnetizations = 0,

        #Complex attributes :
        deathrattles = [],
        dying_effects = [],
        end_turn_effects = [],
        is_attacked_effects = [],
        attacking_effects = [],
        after_attacking_effects = [],
        minion_summoning_effects = [],
        smn_else_dies_effects = [],
        start_combat_effects = [],

        #Shop effects :

        battlecries = [],
        play_minion_effects = [],
        start_turn_effects = [],
        sell_effects = [],
        card_added_effects = [],
        magnetic = False 
)



Minions_dict = {
    #Demons
    'Backstage Security' : Backstage_Security,
    'Soul Rewinder' : Soul_Rewinder,
    'Legion Overseer' : Legion_Overseer,
    #Elementals
    'Sellemental' : Sellemental,
    'Molten Rock' : Molten_Rock,
    #Dragons
    'Low Flier': Low_Flier,
    #Quilboars
    'Prickly Piper' : Prickly_Piper,
    #Undead
    'Risen Rider' : Risen_Rider,
    'Eternal Knight' : Eternal_Knight,
    'Soulsplitter' : Soulsplitter,
    'Eternal Summoner' : Eternal_Summoner,
    'Sister Deathwhisper' : Sister_Deathwhisper,
    #Neutrals
    'Spawn of NZoth': Spawn_of_Nzoth,
    'Leeroy The Reckless' : Leeroy_The_Reckless,

}
