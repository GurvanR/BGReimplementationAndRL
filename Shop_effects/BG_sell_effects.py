from typing import Any, Optional, Union, List, Dict
from random import choice


from BG_primary_objects_definition import Minion
from BG_primary_objects_definition import Warband
from BG_primary_objects_definition import Sell_effect

#default is for getting one coin and lose the minion
class Default_sell_effect(Sell_effect):
    def __init__(self) -> None:
        super().__init__()
    def trigger(self, warband1: Warband, warband2: Warband):
        return super().trigger(warband1, warband2)