from character import skin
from equipment import Equipment
from player import Player
from prompts import print_dict, confirm


def search_location(player: Player):
    if player.location.get_living_monsters():
        print("You can't search the area with live monsters attacking!")
    else:
        if player.location.treasure:
            print(f"You find treasure in {player.location.name}:")
            print_dict(player.location.treasure)
            player.merge_treasure(player.location.treasure)
            player.location.treasure = {}

        if player.location.armor:
            print(f"You find items in {player.location.name}")
            print_dict(player.location.armor)
            armor: Equipment
            for armor in player.location.armor.values():
                use = confirm(f"Use {armor.name}? (y/n)")
                if use:
                    if player.armor is not skin:
                        player.location.armor[player.armor.name] = player.armor
                        player.armor = armor

        dead_monsters = player.location.get_dead_monsters()
        if dead_monsters:
            print(f"You search {len(dead_monsters)} monsters:")
            for i, monster in enumerate(dead_monsters):
                print(f"Monster {i + 1} had:")
                print_dict(monster.treasure)
                player.merge_treasure(monster.treasure)
                monster.treasure = {}
                if monster.armor.power > 0:
                    print(f"A monstor has {monster.armor.name} armor")
                    response = confirm("Use the armor? (y/n)")
                    if response == "y":
                        if player.armor is not skin:
                            player.location.armor[player.armor.name] = player.armor
                        player.armor = monster.armor
                        monster.armor = skin

    print("You have the following treasure:")
    print_dict(player.treasure)
