#1/usr/bin/python
import tiles
from list_items import list_items
def lread(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: read [item]"
        return

    items, things, npc_items =list_items(room, player)

    if commands[1] == "all":
        for item in room.inventory:
            if hasattr(item, "read"):
                print "{}:\n".format(item.shortnames[0])
                item.display()
        return


    if commands[1] not in things:
        print "\tI do not know what a {} is.".format(commands[1])
        return


    if commands[1] in things and commands[1] not in items:
        print "\tYou do not see the {} here.".format(commands[1])
        return
    
    for item in room.inventory:
        if hasattr(item, "opened") and item.opened:
            for sub_item in item.inventory:
                if hasattr(sub_item, "read"):
                    for sname in sub_item.shortnames:
                        if commands[1] == sname:
                            sub_item.display()
                            return

        if hasattr(item, "read"):
            for sname in item.shortnames:
                if commands[1] == sname:
                    item.display()
                    return

    for item in player.inventory:
        if hasattr(item, "read"):
            for sname in item.shortnames:
                if commands[1] == sname:
                    item.display()
                    return

    print "\tYou cannot read the {}".format(commands[1])    
    
