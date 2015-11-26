#1/usr/bin/python
def drop(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: drop [item]"
        return

    if player.inventory is None:
        print "\tThere is nothing to drop!"
        return


    if commands[1] == "all":
        items_dropped =[]
        for item in reversed(player.inventory):
            print player.inventory
            items_dropped.append(item)
            print "\t{} dropped".format(item.shortnames[0])
            if hasattr(item, "wearable"):
                print "\tYou are no longer wearing the {}.".format(commands[1])
                item.worn=False
                player.badged = False
                room.default(player)
                room.available_actions()
                room.exits_text(player)
            player.inventory.remove(item)
            room.inventory.append(item)
        return
    
        # for item in items_dropped:
        #     room.inventory.append(item)

        



    for item in player.inventory:
        
        if commands[1] in item.shortnames:
            
            player.inventory.remove(item)
            print "\t{} dropped".format(item.shortnames[0])
            room.inventory.append(item)
            if hasattr(item, "wearable"):
                print "\tYou are no longer wearing the {}.".format(commands[1])
                item.worn=False
                player.badged = False
                room.default(player)
                room.available_actions()
                room.exits_text(player)
                return

    # if __name__ == "__main__":
    #     trip()
