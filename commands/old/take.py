#1/usr/bin/python
from list_items import list_items

def take(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: take [item]"
        return
    else:
        if room.inventory is None:
            print "\tThere is nothing to take!"
            return


    if commands[1] == "all":
        for item in room.inventory:
            if item.takeable:
                player.inventory.append(item)
                print "\t{} taken".format(item.shortnames[0])
        return




    items, things, npc_items = list_items(room, player)

    if commands[1] not in things:
        print "\tYou cannot take the {}, if there is even really a {} here.".format(commands[1], commands[1])
        return

    if hasattr(room, "npc"):
        for sname in room.npc.shortnames:
            if commands[1] == sname:
                print "You cannot take the {}!".format(room.npc.shortnames[0])
                return

    for owned in player.inventory:
        for sname in owned.shortnames:
            if commands[1] == sname:
                print "\tYou already have the {}.".format(commands[1])
                return

    if commands[1] in things and commands[1] not in items:
        print "\tYou don't see the {} here.".format(commands[1])
        return


    elif commands[1] in things and commands[1] in items:
        for item in room.inventory:
            if hasattr(item, "opened") and item.opened:
                for sub_item in item.inventory:
                    if commands[1] in sub_item.shortnames :
                        if sub_item.takeable:
                            player.inventory.append(sub_item)
                            print "\t{} taken".format(sub_item.shortnames[0])
                            item.inventory.remove(sub_item)
                            return
                        else:
                            print "\tYou cannot take the {}.".format(commands[1])
                            return


            if commands[1] in item.shortnames :
                if item.takeable:
                    player.inventory.append(item)
                    print "\t{} taken".format(item.shortnames[0])
                    room.inventory.remove(item)
                    return
                else:
                    print "\tThe {} is too heavy to move.".format(commands[1])
                    return
    
    

    # if commands[1] in things:
    #     for item in room.inventory:
    #         if commands[1] in item.shortnames :
    #             if item.takeable:
    #                 player.inventory.append(item)
    #                 print "\t{} taken".format(item.shortnames[0])
    #                 room.inventory.remove(item)
    #                 return
    #             else:
    #                 print "\tThe {} is too heavy to move.{}.".format(commands[1])
    #                 return
    #     else:
            
    # else: # not in things
    
    # print "\tYou cannot take the {}.".format(commands[1])

    
# if __name__ == "__main__":
#     trip()
