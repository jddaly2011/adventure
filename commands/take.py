#1/usr/bin/python
from get_item import get_item 

def take(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: take [item]"
        return
    if commands[1] in room.ordinary:
        print "\tYou cannot take the {}.".format(commands[1])
        return
    if not room.inventory:
        print "\tThere is nothing to take!"
        return

    if commands[1] == "all":
        items_to_remove = []
        for npc in room.npcs:
            print "\tYou cannot take the {}.".format(npc.shortnames[0])
        for item in room.inventory:
            if hasattr(item, "opened") and item.opened and item.inventory:
                sub_items_to_remove=[]
                for sub_item in item.inventory:
                    if sub_item.takeable:
                        player.inventory.append(sub_item)
                        sub_items_to_remove.append(sub_item)
                        print "\t{} taken".format(sub_item.shortnames[0])
                    else:
                        print "\tYou cannot take the {}.".format(sub_item.shortnames[0])

                if sub_items_to_remove:
                    for sub_item in sub_items_to_remove:
                        item.inventory.remove(sub_item)
            if item.takeable:
                player.inventory.append(item)
                items_to_remove.append(item)
                print "\t{} taken".format(item.shortnames[0])
#                room.inventory.remove(item)
            else:
                print "\tYou cannot take the {}.".format(item.shortnames[0])
        if items_to_remove:
            for item in items_to_remove:
                room.inventory.remove(item)

            
        return

    item, owner = get_item(room, player, commands[1])# owner = room, player, openable, npc, npc_item

    if not item:
        things = owner

        if commands[1] not in things:
            print "\tI do not know the word {}.".format(commands[1])
            return

        if commands[1] in things:
            print "\tYou don't see the {} here.".format(commands[1])
            return

    if owner == "npc":
        print "You cannot take the {}!".format(commands[1])
        return

    if owner == "npc_item":
        print "The {} declines to give you the {}!".format(item.name, commands[0])
        return

    if owner == "player":
        print "\tYou already have the {}.".format(commands[1])
        return

    if owner == "room":
        if item.takeable:
            player.inventory.append(item)
            print "\t{} taken".format(item.shortnames[0])
            room.inventory.remove(item)
            return
        else:
            print "\tThe {} is too heavy to move.".format(commands[1])
            return

    if owner == "openable":
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


