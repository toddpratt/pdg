from collections import defaultdict

from character import CharacterMixin
from location import Location


class Player(CharacterMixin):

    def __init__(self, hp: int, power: int, location: Location):
        super().__init__(hp, power)
        self.location = location
        self.treasure = defaultdict(int)

    def merge_treasure(self, treasure):
        for k in treasure:
            self.treasure[k] += treasure[k]
