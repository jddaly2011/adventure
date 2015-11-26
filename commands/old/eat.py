#1/usr/bin/python
from list_items import list_items

def eat(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: eat [item]"
        return
    else:
        if room.inventory is None:
            print "\tThere is nothing to eat!"
            return

    items, things, npc_items = list_items(room, player)

    if commands[1] not in things:
        print "\tYou cannot eat the {}, if there is even really a {} here.".format(commands[1], commands[1])
        return


    if commands[1] in things and commands[1] not in items:
        print "\tYou don't see the {} here.".format(commands[1])
        return

    for owned in player.inventory:
        for sname in owned.shortnames:
            if commands[1] == sname:
                if hasattr(owned, "eatable"):
                    print "\tYou have eaten the {}. It was so-so".format(commands[1])
                    player.inventory.remove(owned)
                    owned.eaten = True
                    player.eaten.append(owned)
                    print player.eaten
                    return
                else:
                    print "\tThe {} is not edible.".format(commands[1])




 
    for item in room.inventory:
        if hasattr(item, "opened") and item.opened:
            for sub_item in item.inventory:
                if commands[1] in sub_item.shortnames :
                    if hasattr(sub_item, "eatable"):
                        item.inventory.remove(sub_item)
                        print "\t{} eaten".format(sub_item.shortnames[0])
                        sub_item.eaten = True
                        player.eaten.append(sub_item)
                        print player.eaten

                        return
                    else:
                        print "\tYou cannot eat the {}.".format(commands[1])
                        return


        if commands[1] in item.shortnames :
            if hasattr(item, "eatable"):
                print "\t{} you ate it".format(item.shortnames[0])
                room.inventory.remove(item)
                item.eaten = True
                player.eaten.append(owned)
                print player.eaten

                return
            else:
                print "\tThe {} is not edible.".format(commands[1])
                return


    
# if __name__ == "__main__":
#     trip()
