from random import randint


class CharacterMixin:

    def __init__(self, hp: int, power: int):
        self.hp: int = hp
        self.power: int = power

    def strike_power(self):
        return randint(1, self.power)

    def take_damage(self, damage):
        self.hp -= damage
