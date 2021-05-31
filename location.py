from typing import Sequence, Mapping

from monster import Monster
from passage import Passage


class Location:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.passages: Mapping[str, Passage] = {}
        self.treasure = {}
        self.monsters = []
        self.armor = {}

    def get_living_monsters(self) -> Sequence[Monster]:
        monsters = [m for m in self.monsters if m.hp > 0]
        return monsters

    def get_dead_monsters(self) -> Sequence[Monster]:
        monsters = [m for m in self.monsters if m.hp < 1]
        return monsters

    def enter(self, player):
        pass


class Trap(Location):

    def enter(self, player):
        player.hp = 0
