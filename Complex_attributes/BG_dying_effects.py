from typing import Any, Optional, Union, List, Dict
from random import choice


from BG_primary_objects_definition import Minion
from BG_primary_objects_definition import Warband
from BG_primary_objects_definition import Dying_effect

#Dying_effects : 
class default(Dying_effect):
    def __init__(self) -> None:
        pass
    def trigger(self, warband1: Warband, warband2 :Warband, death_pos: int = None, minion: Minion = None):
        pass

class Eternal_Knight(Dying_effect):
    def __init__(self) -> None:
        pass
    def trigger(self, warband1: Warband, warband2 :Warband, death_pos: int = None, minion: Minion = None):
        warband1.eternal_counter +=1
        eternals = [minion for minion in warband1 if minion.name == 'Eternal Knight']
        for minion in eternals :
            minion.atk+=1
            minion.health+=1