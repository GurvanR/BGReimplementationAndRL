from typing import Any, Optional, Union, Dict
from random import choice


from BG_primary_objects_definition import Minion, Warband, Deathrattle


class summon(Deathrattle):
    def __init__(self, minions_summoned: list[Minion] ) -> None:
        super().__init__()
        self.minions_summoned = minions_summoned #Minions to summon.

    def trigger(self, warband1: Warband, warband2: Warband, death_pos: int = None, minion = None) -> None :
        if death_pos is None : death_pos = warband1.index(self)
        for minion in self.minions_summoned:
                warband1.summon(minion, warband1[self.death_pos]) #The minions are summoned at the place the deathrattle minion died.

class Trickster(Deathrattle):
    def __init__(self) -> None:
        super().__init__()

    def trigger(self, warband1: Warband, warband2: Warband, death_pos = None, minion = None ) -> None :
        choice(warband1).health += minion.health



class NZoth(Deathrattle):
    def __init__(self) -> None:
        super().__init__()

    def trigger(self, warband1: Warband, warband2: Warband, death_pos = None, minion = None) -> None :
        for minion in warband1 :
            minion.health += 1
            minion.atk    += 1
