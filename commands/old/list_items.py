#1/usr/bin/python
def list_items(room, player):
    items =[]
    for item in room.inventory:
        if hasattr(item, "opened") and item.opened:
            for sub_item in item.inventory:
                for sname in sub_item.shortnames:
                    items.append(sname)
        for sname in item.shortnames:
            items.append(sname)

#    playerItems =[]
    for item in player.inventory:
        for sname in item.shortnames:
            items.append(sname)


    with open("things", "r") as f:
        things = f.read()
        f.close()
        things = things.split("\n")
        things = filter(None, things)

    npc_items =[]
    if room.npcs:
        for npc in room.npcs:
            if npc.inventory:
                for item in npc.inventory:
                    for sname in item.shortnames:
                        npc_items.append(sname)

    return(items, things, npc_items)
    
    

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
