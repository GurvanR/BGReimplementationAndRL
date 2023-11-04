from typing import Any, Optional, Union, List, Dict
from random import choice


from BG_primary_objects_definition import Minion
from BG_primary_objects_definition import Warband
from BG_primary_objects_definition import Play_minion_effect


#faire un default play effect that adds the minion at a certain position in the Warband ?

class Molten_Rock(Play_minion_effect):
    def __init__(self) -> None:
        super().__init__()
    def trigger(self, warband1: Warband, warband2: Warband):
        return super().trigger(warband1, warband2)

class Kalecgos_Arcane_Aspect(Play_minion_effect):
    def __init__(self) -> None:
        super().__init__()
    def trigger(self, warband1: Warband, warband2: Warband):
        return super().trigger(warband1, warband2)