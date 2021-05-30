

class Location:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.locations = {}
        self.treasure = {}
        self.monsters = []

    def get_living_monsters(self):
        monsters = [m for m in self.monsters if m.hp > 0]
        return monsters

    def get_dead_monsters(self):
        monsters = [m for m in self.monsters if m.hp < 1]
        return monsters

    def enter(self, player):
        pass


class Trap(Location):

    def enter(self, player):
        player.hp = 0
