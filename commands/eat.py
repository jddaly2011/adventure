#1/usr/bin/python
from get_item import get_item 

def eat(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: eat [item]"
        return
    if commands[1] in room.ordinary:
        print "\tYou cannot eat the {}.".format(commands[1])
        return

    item, owner = get_item(room, player, commands[1])# owner = room, player, openable, npc, npc_item


    if not item:
        things = owner

        if commands[1] not in things:
            print "\tYou cannot eat the {}, if there is even really a {} here.".format(commands[1], commands[1])
            return
        else:
            print "\tYou don't see the {} here.".format(commands[1])
            return

    if owner == "player":
        if hasattr(item, "eatable"):
            print "\tYou have eaten the {}. It was so-so".format(commands[1])
            player.inventory.remove(item)
            item.eaten = True
            player.eaten.append(item)
            return
        else:
            print "\tThe {} is not edible.".format(commands[1])
            return


    if owner == "room":
        if hasattr(item, "eatable"):
            print "\tYou have eaten the {}. It was so-so".format(commands[1])
            room.inventory.remove(item)
            item.eaten = True
            player.eaten.append(item)
            return
        else:
            print "\tThe {} is not edible.".format(commands[1])
            return


    if owner == "openable":
        for sub_item in item.inventory:
            if commands[1] in sub_item.shortnames :
                if hasattr(sub_item, "eatable"):
                    item.inventory.remove(sub_item)
                    print "\t{} eaten".format(sub_item.shortnames[0])
                    sub_item.eaten = True
                    player.eaten.append(sub_item)
                    return
                else:
                    print "\tYou cannot eat the {}.".format(commands[1])
                    return


    if owner == "npc_item":
            print "\tThe {} decliens to let you eat the {}.".format(item.shortnames[0], commands[1])
            return


    if owner == "npc":
            print "\tYou cannot eat the {}!".format(commands[1])
            return

    
# if __name__ == "__main__":
#     trip()


