from typing import Sequence

from commands.search import search_location
from locations.big_room import get_big_room
from locations.corridor import get_corridor
from monster import Monster
from passage import Passage
from player import Player
from location import Location
from prompts import print_dict


def create_game() -> Player:

    entrance = Location(
        name='entrance',
        description="You are the entrance of scary cave.")

    corridor = get_corridor()
    big_room = get_big_room()

    # Link Rooms Together
    big_room.passages[corridor.name] = Passage("Corridor leading to entrance.", corridor)
    corridor.passages['door'] = Passage("Large wooden door.", big_room)
    entrance.passages[corridor.name] = Passage("Entrance to a long corridor", corridor)
    corridor.passages[entrance.name] = Passage("Way out to the entrance", entrance)

    player = Player(20, 10, entrance)
    return player


def loop(player: Player):
    while True:
        print(player.location.description)
        monsters = player.location.get_living_monsters()
        if monsters:
            print("You are not alone here!")
            print(f"{len(monsters)} monsters attack.")
            print("Enter a location to run or 'attack' to attack.")

        print("paths:")
        for name, passage in player.location.passages.items():
            print(f"  {name} - {passage.description}")

        command = input("> ")

        if command == 'attack':
            if monsters:
                fight(player, monsters)
            else:
                print("No monsters to attack")

        elif command == 'inv':
            print_dict(player.treasure)

        elif command == 'search':
            search_location(player)

        elif command.startswith("take "):
            target = command.split()[1]


        elif command.startswith("open "):
            location = command.split()[1]
            player.navigate(location)

        else:
            player.navigate(command)


def fight(player: Player, monsters: Sequence[Monster]):
    for monster in monsters:
        monster.take_damage(player.strike_power())
        if monster.hp < 1:
            print("A monster dies!")
        else:
            player.take_damage(monster.strike_power())
            if player.hp < 1:
                print("You died!")


if __name__ == "__main__":
    loop(create_game())
