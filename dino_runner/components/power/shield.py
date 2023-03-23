from dino_runner.utils.constants import SHIELD, SHIELD_TYPE #SHIELD_Type seria inecessario
from dino_runner.components.power.power import *

class Shield(Power):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)