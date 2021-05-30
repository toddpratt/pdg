from random import randint

from equipment import Equipment


skin = Equipment('skin', 0)


class CharacterMixin:

    def __init__(self, hp: int, power: int):
        self.hp: int = hp
        self.power: int = power
        self.armor: Equipment = skin
        self.weapon: Equipment = Equipment('dagger', 2)

    def strike_power(self) -> int:
        return randint(1, self.power + self.weapon.power)

    def take_damage(self, damage: int):
        if damage > self.armor.power:
            self.hp -= damage - self.armor.power
