from equipment import Equipment
from location import Location
from monster import Monster


def get_corridor() -> Location:
    corridor = Location(
        name='corridor',
        description="You are in a corridor leading to a large wooden door.")
    corridor.treasure = {
        'gold': 3
    }
    corridor_monster = Monster(hp=5, power=4, treasure={'gold': 4})
    corridor_monster.armor = Equipment('chainmail', 4)
    corridor.monsters.append(corridor_monster)
    plate = Equipment('platemail', 8)
    corridor.armor[plate.name] = plate
    return corridor
