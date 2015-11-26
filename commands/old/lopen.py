#1/usr/bin/python
def lopen(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: open [item]"
        return
    else:
        if room.inventory is None:
            print "\tThere is nothing to open!"
            return

    items =[]
    for item in room.inventory:
        for sname in item.shortnames:
            items.append(sname)


    with open("things", "r") as f:
        things = f.read()
        f.close()
        things = things.split("\n")
        things = filter(None, things)


    if commands[1] not in things:
        print "\tYou cannot open the {}, if there is even really a {} here.".format(commands[1], commands[1])
        return

    if commands[1] in things and commands[1] not in items:
        print "\tYou don't see the {} here.".format(commands[1])
        return


    elif commands[1] in things and commands[1] in items:
        for item in room.inventory:
            if commands[1] in item.shortnames :
                if hasattr(item, "opened"):
                    if item.opened:
                        print "\tThe {} is already open".format(commands[1])
                        return
                    else:
                        item.opened=True
                        print "\t{} opened".format(commands[1])
                        for thing in item.inventory:
                            print "\tThere is {} here.".format(thing.name)
                        return
            else:
                print "\tYou cannot open the {}.".format(commands[1])
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
