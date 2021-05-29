from typing import Sequence

from monster import Monster
from player import Player
from location import Location


def create_game() -> Player:

    root = Location(
        name='entrance',
        description="You are the entrance of scary cave.")

    corridor = Location(
        name='corridor',
        description="You are in a corridor leading to a large wooden door.")
    corridor.treasure = {
        'gold': 3
    }

    corridor.monsters.append(
        Monster(
            hp=5,
            power=4,
            treasure={
                'gold': 4
            }
        )
    )

    root.locations[corridor.name] = corridor
    corridor.locations[root.name] = root
    player = Player(20, 10, root)
    return player


def loop(player: Player):
    while True:
        print(player.location.description)
        monsters = player.location.get_living_monsters()
        if monsters:
            print("You are not alone here!")
            print(f"{len(monsters)} monsters attack.")
            print("Enter a location to run or 'attack' to attack.")

        print("locations: " + ", ".join(player.location.locations.keys()))
        command = input("> ")

        if command == 'attack':
            if monsters:
                fight(player, monsters)
            else:
                print("No monsters to attack")
        elif command == 'search':
            if monsters:
                print("You can't search the area with live monsters attacking!")
            else:
                dead_monsters = player.location.get_dead_monsters()
                if player.location.treasure:
                    print(f"You find treasure in {player.location.name}:")
                    print_treasure(player.location.treasure)
                    player.merge_treasure(player.location.treasure)
                    player.location.treasure = {}

                if dead_monsters:
                    print(f"You search {len(dead_monsters)} monsters:")
                    for i, monster in enumerate(dead_monsters):
                        print(f"Monster {i + 1} had:")
                        print_treasure(monster.treasure)
                        player.merge_treasure(monster.treasure)
                        monster.treasure = {}
            print("You have the following treasure:")
            print_treasure(player.treasure)
        else:
            try:
                player.location = player.location.locations[command]
            except KeyError:
                print(f"The location '{command}' doesn't seem to exist.")


def fight(player: Player, monsters: Sequence[Monster]):
    for monster in monsters:
        monster.take_damage(player.strike_power())
        if monster.hp < 1:
            print("A monster dies!")
        else:
            player.take_damage(monster.strike_power())
            if player.hp < 1:
                print("You died!")


def print_treasure(treasure):
    for k in treasure:
        print(f"    {treasure[k]} {k}")


if __name__ == "__main__":
    loop(create_game())
