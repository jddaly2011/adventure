#1/usr/bin/python
import tiles
from get_item import get_item 

def examine(commands, available_actions, player, room):
    if commands[0] == "examine" and len(commands) < 2:
        print "\tUsage: examine [item]"
        return

    if commands[1] == "all":
        for item in room.inventory:
            print "\t{}: {}".format(item.shortnames[0], item.description)

        if room.npcs:
            for npc in room.npcs:
                print "\t{}: {}".format(npc.shortnames[0], npc.description)
                if npc.inventory:
                    print "\t{} appears to be holding:".format(npc.name)
                    for item in npc.inventory:
                        print "\t{}".format(item.name)
        return

    if commands[1] in room.ordinary:
        print "\tIt is an ordinary {}.".format(commands[1])
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


    if owner == "npc_item":
        for npc in room.npcs:
            if npc.inventory:
                for item in npc.inventory:
                    for sname in item.shortnames:
                        if commands[1] == sname:
                            print "\t{} declines to show you the {}".format(npc.name, commands[1])
                            return


    else: 
        print item.description
        return
    
    

    # if player.inventory is not None and commands[1] in things:
    #     for item in player.inventory:#room.inventory:
    #         if commands[1] in item.shortnames:
    #             player.describe_an_item(item)
    #             return
    #     else:
    #         print "\tYou do not have {}".format(commands[1])
    #         return
      
    # if commands[0] == "examine" and len(commands) > 1:
    #     print "\tIt is a {}".format(commands[1])
    #     return
         

    # print "You have tripped in {}".format(room.room_name())
    
# if __name__ == "__main__":
#     trip()

