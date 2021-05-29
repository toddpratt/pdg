from character import CharacterMixin


class Monster(CharacterMixin):

    def __init__(self, hp, power, treasure):
        super().__init__(hp, power)
        self.treasure: dict = treasure
