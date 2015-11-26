#1/usr/bin/python
def drop(commands, available_actions, player, room):
    if len(commands) < 2:
        print "\tUsage: drop [item]"
        return

    if player.inventory is None:
        print "\tThere is nothing to drop!"
        return

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
                room.exits_text()
                return

    # if __name__ == "__main__":
    #     trip()
